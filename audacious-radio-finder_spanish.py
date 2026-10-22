#!/usr/bin/env python3
"""Radio Browser search for Audacious. Python standard library + YAD + curl by pp4mnk"""
import json
import shutil
import subprocess
import sys
import urllib.parse
from concurrent.futures import ThreadPoolExecutor

TITLE = 'Audacious Radio Finder'
SERVERS = ['https://de1.api.radio-browser.info', 'https://de2.api.radio-browser.info']


def dialog(*args, data=None):
    return subprocess.run(['yad', '--title=' + TITLE, '--center', '--no-markup',
                           *args], input=data, text=True, stdout=subprocess.PIPE)


def message(text):
    dialog('--info', '--width=520', '--text=' + text)


def request(server, path):
    result = subprocess.run(['curl', '--fail', '--silent', '--show-error',
                             '--location', '--connect-timeout', '5', '--max-time', '15',
                             '--max-filesize', '8000000', '-A', TITLE.replace(' ', '-') + '/1.0',
                             server + path], capture_output=True, text=True)
    if result.returncode:
        raise RuntimeError(result.stderr.strip() or 'Error de conexión')
    return json.loads(result.stdout)


def search(params):
    errors = []
    for server in SERVERS:
        try:
            rows = request(server, '/json/stations/search?' + urllib.parse.urlencode(params))
            if not isinstance(rows, list):
                raise ValueError('La respuesta no contiene una lista')
            return server, [r for r in rows if isinstance(r, dict)]
        except (RuntimeError, ValueError) as exc:
            errors.append(str(exc))
    raise RuntimeError('\n'.join(errors))


def clean(value):
    return ' '.join(str(value or '').split())


def main():
    for tool in ('yad', 'curl', 'audacious'):
        if not shutil.which(tool):
            print('Falta el programa: ' + tool, file=sys.stderr)
            return 1
    values = ['', '', '', '']
    while True:
        fields = ['--form', '--width=580', '--separator=\n',
                  '--text=Busca en Radio Browser. Puedes combinar campos.\n'
                  'País e idioma: usa Spain, France, spanish, english…\n'
                  'Género: jazz, rock, classical… Máximo 200 resultados.',
                  '--button=Salir:1', '--button=Buscar:0']
        for label, value in zip(('Nombre', 'País', 'Idioma', 'Género / etiqueta'), values):
            fields.extend(['--field=' + label, value])
        result = dialog(*fields)
        if result.returncode != 0:
            return 0
        values = result.stdout.rstrip('\n').split('\n')
        values = (values + [''] * 4)[:4]
        params = dict(zip(('name', 'country', 'language', 'tag'),
                          (v.strip() for v in values)))
        params = {k: v for k, v in params.items() if v}
        if not params:
            message('Escribe al menos un criterio de búsqueda.')
            continue
        params.update(limit=200, hidebroken='true', order='clickcount', reverse='true')
        with ThreadPoolExecutor(max_workers=1) as pool:
            task = pool.submit(search, params)
            progress = subprocess.Popen(['yad', '--progress', '--pulsate', '--no-buttons',
                                         '--undecorated', '--center', '--text=Buscando emisoras…'],
                                        stdin=subprocess.PIPE, stdout=subprocess.DEVNULL)
            try:
                server, rows = task.result()
            except Exception as exc:
                rows = None
                error = str(exc)
            finally:
                if progress.poll() is None:
                    progress.terminate()
                progress.communicate()
        if rows is None:
            message('No se pudo consultar Radio Browser.\n' + error)
            continue
        if not rows:
            message('Sin resultados. Prueba con menos filtros o con otro nombre.')
            continue
        data = ''.join('\n'.join([str(i), clean(r.get('name')), clean(r.get('country')),
                                  clean(r.get('language')), clean(r.get('codec')),
                                  clean(r.get('bitrate'))]) + '\n'
                       for i, r in enumerate(rows))
        while True:
            selected = dialog('--list', '--width=900', '--height=540',
                              '--text=Doble clic para reproducir en Audacious.\n'
                              'Selecciona la lista y escribe para buscar por nombre.',
                              '--column=ID:HD', '--column=Emisora', '--column=País',
                              '--column=Idioma', '--column=Formato', '--column=kb/s',
                              '--search-column=2', '--print-column=1', '--separator=',
                              '--button=Nueva búsqueda:2', '--button=Cerrar:1',
                              '--button=Reproducir:0', data=data)
            if selected.returncode == 2:
                break
            if selected.returncode != 0:
                return 0
            try:
                station = rows[int(selected.stdout.strip())]
            except (ValueError, IndexError):
                message('Selecciona una emisora de la lista.')
                continue
            url = station.get('url_resolved') or station.get('url') or ''
            if urllib.parse.urlsplit(url).scheme not in ('http', 'https'):
                message('Esta emisora no proporciona una dirección HTTP/HTTPS válida.')
                continue
            subprocess.Popen(['audacious', url], start_new_session=True,
                             stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            # Notify Radio Browser of an actual playback click, without delaying the UI.
            uid = station.get('stationuuid')
            if uid:
                subprocess.Popen(['curl', '--silent', '--fail', '--max-time', '5',
                                  '-A', 'Audacious-Radio-Finder/1.0',
                                  server + '/json/url/' + urllib.parse.quote(uid, safe='')],
                                 stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


if __name__ == '__main__':
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        sys.exit(0)
