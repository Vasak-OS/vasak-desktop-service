from Lynx.Master import LynxMaster
from Lynx.Notifications import Notifications
from gi.repository import GLib
from dbus.mainloop.glib import DBusGMainLoop


if __name__ == "__main__":
    DBusGMainLoop(set_as_default=True)
    loop = GLib.MainLoop()

    lynxNotify = Notifications()
    lScreen = LynxMaster(lynxNotify)

    loop.run()

