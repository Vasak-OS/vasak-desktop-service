# Vasak Desktop Service

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=Vasak-OS_vasak-desktop-service&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=Vasak-OS_vasak-desktop-service)

Vasak is a desktop service that provides a simple way to manage your desktop (DBUS and Python Scripts). It is written in Python and uses GTK+ and DBUS. It is designed to be simple and easy to use.

## Features

* DBUS Service
* Python Scripts
* Windows Change Data
* Simple and easy to use

## Dependencies

* python
* python-gobject
* python-dbus
* gnome-menus
* libwnck3
* libxkbcommon-x11

## Start Vasak Desktop Service

To start Vasak Desktop Service, run the following steps:

1. Clone the repository

```bash
git clone git@github.com:Vasak-OS/vasak-desktop-service.git
```

2. Move to the directory

```bash
cd vasak-desktop-service
```

3. Start

```bash
python main.py
```

## Build Vasak Desktop Service

[PKGBUILD](https://github.com/Vasak-OS/PKGBUILDS/blob/main/vasak-desktop-service/PKGBUILD)


## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. Please make sure to update tests as appropriate.

1. Fork it
2. Create your feature branch

```bash
git checkout -b feature/my-new-feature
```

3. Commit your changes 

```bash
git commit -am 'Add some my-new-feature'
```

4. Push to the branch

```bash
git push origin feature/my-new-feature
```

5. Create a new Pull Request

