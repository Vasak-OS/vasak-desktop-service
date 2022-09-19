from Vasak.Master import VasakMaster
from Vasak.Notifications import Notifications
from gi.repository import GLib
from dbus.mainloop.glib import DBusGMainLoop


if __name__ == "__main__":
    DBusGMainLoop(set_as_default=True)
    loop = GLib.MainLoop()

    vasakNotify = Notifications()
    lScreen = VasakMaster(vasakNotify)

    loop.run()
