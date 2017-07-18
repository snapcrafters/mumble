## APT Dependencies

* libavahi-compat-libdnssd1
* libg15daemon-client1

## Link to Mumble Issue

https://github.com/mumble-voip/mumble/issues/3177

## Issues

* Upon launch, I have a popup that states:

```
Mumble failed to initialize a database in any of the possible locations
```

* Terminal Output on launch:

```
QGtkStyle could not resolve GTK. Make sure you have installed the proper libraries.
Qt: Session management error: None of the authentication protocols specified are supported
ALSA lib conf.c:3750:(snd_config_update_r) Cannot access file /usr/share/alsa/alsa.conf
ALSAEnumerator: Namehint not found
ALSA lib conf.c:3750:(snd_config_update_r) Cannot access file /usr/share/alsa/alsa.conf
ALSAEnumerator: snd_device_name_hint: -2
ALSA lib conf.c:3750:(snd_config_update_r) Cannot access file /usr/share/alsa/alsa.conf
G15LCDEngineUnix: Unable to connect to G15Daemon.
CELT bitstream 8000000b from /snap/mumble/x1/bin/libcelt0.so.0.7.0
CELT bitstream 80000010 from /snap/mumble/x1/bin/libcelt0.so.0.11.0
Locale is "en_CA" (System: "en_CA")
TextToSpeech: Failed to contact speech dispatcher.
QSqlDatabase: QSQLITE driver not loaded
QSqlDatabase: available drivers:
Database: Failed initialization
Aborted (core dumped)
```

Latest:

```
(process:4388): Gtk-WARNING **: Locale not supported by C library.
	Using the fallback 'C' locale.
Gtk-Message: Failed to load module "gail"
Gtk-Message: Failed to load module "atk-bridge"
Gtk-Message: Failed to load module "canberra-gtk-module"
Qt: Session management error: None of the authentication protocols specified are supported
ALSA lib conf.c:3750:(snd_config_update_r) Cannot access file /usr/share/alsa/alsa.conf
ALSAEnumerator: Namehint not found
ALSA lib conf.c:3750:(snd_config_update_r) Cannot access file /usr/share/alsa/alsa.conf
ALSAEnumerator: snd_device_name_hint: -2
ALSA lib conf.c:3750:(snd_config_update_r) Cannot access file /usr/share/alsa/alsa.conf
G15LCDEngineUnix: Unable to connect to G15Daemon.
CELT bitstream 8000000b from /snap/mumble/x1/bin/libcelt0.so.0.7.0
CELT bitstream 80000010 from /snap/mumble/x1/bin/libcelt0.so.0.11.0
Locale is "en_CA" (System: "en_CA")
TextToSpeech: Failed to contact speech dispatcher.
QSqlDatabase: QSQLITE driver not loaded
QSqlDatabase: available drivers:

(mumble:4388): GdkPixbuf-WARNING **: Cannot open pixbuf loader module file '/usr/lib/x86_64-linux-gnu/gdk-pixbuf-2.0/2.10.0/loaders.cache': No such file or directory

This likely means that your installation is broken.
Try running the command
  gdk-pixbuf-query-loaders > /usr/lib/x86_64-linux-gnu/gdk-pixbuf-2.0/2.10.0/loaders.cache
to make things work again for the time being.
Database: Failed initialization
Aborted (core dumped)
```
