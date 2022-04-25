from Lynx.Screen import LynxScreen
from Lynx.DBus import client
from Lynx.Notifications import Notifications
from gi.repository import GLib
from dbus.mainloop.glib import DBusGMainLoop


if __name__ == "__main__":
    DBusGMainLoop(set_as_default=True)
    loop = GLib.MainLoop()

    dockDBus = client('ar.net.lynx.os.dock')

    lynxNotify = Notifications()
    lScreen = LynxScreen(dockDBus, lynxNotify)

    loop.run()

