# Audacious-Radio-Finder
 Audacious Radio Finder, una pequeña herramienta pensada para EasyOS que permite buscar esmisoras de radio por Internet y reproducirla en Audacious desde una interfaz sencilla.  Audacious Radio Finder, a small tool designed for EasyOS that lets you search for Internet radio stations and play them in Audacious through a simple interface.

The idea is to discover and listen to stations without having to open a website, find the audio stream address and copy it into your player manually.

---------

inder: busca emisoras de todo el mundo y escúchalas en Audacious

Comparto Audacious Radio Finder, una pequeña herramienta pensada para EasyOS que permite buscar emisoras de radio por Internet y reproducirlas en Audacious desde una interfaz sencilla.

La idea es poder descubrir y escuchar emisoras sin tener que abrir una web, localizar la dirección del audio y copiarla manualmente al reproductor.

¿Qué permite hacer?

Buscar emisoras por nombre.

Combinar filtros de país, idioma y género o etiqueta.

Consultar hasta 200 resultados por búsqueda.

Ver el país, idioma, formato de audio y bitrate indicado por el catálogo.

Reproducir una emisora haciendo doble clic o pulsando Reproducir.

Volver a buscar mientras Audacious continúa reproduciendo.

Las emisoras se consultan en Radio Browser, un catálogo comunitario en línea. No necesitas crear una lista manualmente ni registrarte para utilizar el programa.

¿Cómo funciona?

El programa está escrito en Python 3 y utiliza YAD para mostrar las ventanas y curl para consultar el catálogo. Al seleccionar una emisora, envía su dirección de audio a Audacious, que se encarga de reproducirla.

Radio Finder actúa como buscador y lanzador: el volumen, la pausa y los demás controles de reproducción siguen estando en Audacious.

Instalación y uso

Instala el paquete .pet correspondiente al idioma que prefieras haciendo clic sobre él en ROX y aceptando la instalación.

Después abre:

Menú → Multimedia → Audacious Radio Finder

Escribe, por ejemplo, Zaragoza en el campo del nombre y pulsa Buscar. También puedes dejar el nombre vacío y buscar jazz en género, o combinarlo con Spain en país.

Para los países e idiomas conviene utilizar los nombres habituales del catálogo, como Spain, France, spanish o english. Si no encuentras resultados, prueba con menos filtros.

El programa necesita Python 3, YAD, curl, Audacious y conexión a Internet. Incluye su propio logo y un acceso en Multimedia.

¿Por qué puede resultar útil?

Puede servir para descubrir música de otros países, escuchar noticias locales, practicar idiomas o encontrar una emisora que acompañe mientras trabajamos. Además, aprovecha Audacious si ya lo utilizamos como reproductor habitual.

Desinstalación

Abre el gestor de paquetes de EasyOS, PKGget, entra en la sección de desinstalación y busca audacious-radio-finder. Selecciona el paquete instalado y confirma su eliminación.

Esto desinstala Radio Finder; Audacious permanece instalado.

Si el menú no refleja una instalación o desinstalación, ejecuta fixmenus en una terminal y reinicia JWM desde el menú de EasyOS.

Una observación: los datos del catálogo y la disponibilidad de las emisiones pueden cambiar. Algunas emisoras podrían estar fuera de servicio o utilizar formatos que requieran complementos adicionales de Audacious.

¡Los comentarios y las pruebas en otros equipos serán bienvenidos!

pp4mnk

English

Audacious Radio Finder: discover worldwide radio stations and listen with Audacious

I’m sharing Audacious Radio Finder, a small tool designed for EasyOS that lets you search for Internet radio stations and play them in Audacious through a simple interface.

The idea is to discover and listen to stations without having to open a website, find the audio stream address and copy it into your player manually.

What can it do?

Search for stations by name.

Combine country, language and genre or tag filters.

Display up to 200 results per search.

Show the country, language, audio format and bitrate reported by the directory.

Play a station by double-clicking it or pressing Play.

Start another search while Audacious continues playing.

Stations come from Radio Browser, an online community directory. There is no need to build a station list manually or register to use the program.

How does it work?

The program is written in Python 3 and uses YAD for its graphical dialogs and curl to query the directory. When you select a station, it passes the audio stream address to Audacious for playback.

Radio Finder handles searching and launching stations. Volume, pause and other playback controls remain in Audacious.

Installation and use

Click the .pet package for your preferred language in ROX and accept the installation.

Then open:

Menu → Multimedia → Audacious Radio Finder

For example, enter Zaragoza in the name field and press Search. Alternatively, leave the name empty and enter jazz in the genre field, or combine it with Spain in the country field.

For countries and languages, use common directory names such as Spain, France, spanish or english. If you get no results, try fewer filters.

The program requires Python 3, YAD, curl, Audacious and an Internet connection. It includes its own logo and a Multimedia menu entry.

Why might it be useful?

It can help you discover music from other countries, listen to local news, practise languages or find something to enjoy while working. It also makes use of Audacious if that is already your preferred audio player.

Uninstallation

Open PKGget, the EasyOS package manager, go to the uninstall section and search for audacious-radio-finder. Select the installed package and confirm its removal.

This removes Radio Finder; Audacious stays installed.

If the menu does not reflect an installation or removal, run fixmenus in a terminal and restart JWM from the EasyOS menu.

Please note: directory information and stream availability can change. Some stations may be offline or use formats that require additional Audacious plugins.

Feedback and reports from other machines are welcome!

pp4mnk
