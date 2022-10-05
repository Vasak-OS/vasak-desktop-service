import Vasak.Icons as icons
from datetime import datetime
from gi.repository import Wnck
import gi
import json
import dbus
import json
import dbus.service as service
gi.require_version('Wnck', '3.0')


class VasakMaster(dbus.service.Object):

    def __init__(self, notify):
        self.minimized_windows = []
        self.notify = notify
        bus_name = service.BusName(
            "ar.net.vasak.os.desktop.service", dbus.SessionBus())
        service.Object.__init__(
            self, bus_name, "/ar/net/vasak/os/desktop/service")
        self.get_screen().connect('window-opened', self.window_open_cb)
        self.get_screen().connect('window-closed', self.window_closed_cb)

    def get_screen(self):
        return Wnck.Screen.get(0)

    def window_open_cb(self, screen, window):
        self.sendWindwosToDesktop()

    def window_closed_cb(self, screen, closed_window):
        for w in self.minimized_windows:
            if w is closed_window:
                self.minimized_windows.remove(closed_window)
        self.sendWindwosToDesktop()

    def sendWindwosToDesktop(self):
        windows = self.get_windows_to_desktop()
        self.updateWindows(windows)

    @dbus.service.signal('ar.net.vasak.os.desktop.service', signature='s')
    def updateWindows(self, windows):
        return str(windows)

    def nameValid(self, name):
        return (name != 'navale' and
                name != 'vasak-desktop' and
                name != 'hydriam')

    def get_windows_to_desktop(self):
        temp_list = []
        for win in self.get_windows():
            if (win.get_window_type() < 1 and
                    self.nameValid(win.get_class_instance_name())):
                datawin = {
                    "name": win.get_class_instance_name().replace("-", " "),
                    "id": win.get_xid(),
                    "icon": icons.get(win.get_class_instance_name())
                }
                temp_list.append(datawin)

        return (json.dumps(temp_list))

    def get_windows(self):
        return self.get_screen().get_windows()

    @dbus.service.method('ar.net.vasak.os.desktop.service', in_signature='s', out_signature='')
    def toggleWindow(self, idWindow):
        for win in self.get_windows():
            if win.get_xid() == int(idWindow):
                if win.is_minimized():
                    win.unminimize(datetime.timestamp(datetime.now()))
                else:
                    win.minimize()

    @dbus.service.method('ar.net.vasak.os.desktop.service', in_signature='', out_signature='s')
    def getNotifications(self):
        return str(self.notify.getNotifications())

    @dbus.service.method('ar.net.vasak.os.desktop.service', in_signature='s', out_signature='')
    def addNotification(self, noti):
        print(noti)
        self.notify.addNotification(json.loads(noti))
