import gi
gi.require_version('Wnck', '3.0')

from dbus import service
import dbus
import json
from vasak import icons
from gi.repository import Wnck
from datetime import datetime



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
        self.send_windwos_to_desktop()

    def window_closed_cb(self, screen, closed_window):
        for win in self.minimized_windows:
            if win is closed_window:
                self.minimized_windows.remove(closed_window)
        self.send_windwos_to_desktop()

    def send_windwos_to_desktop(self):
        windows = self.get_windows_to_desktop()
        self.update_windows(windows)

    @dbus.service.signal('ar.net.vasak.os.desktop.service', signature='s')
    def update_windows(self, windows):
        return str(windows)

    def name_valid(self, name):
        return (name != 'navale' and
                name != 'vasak-desktop' and
                name != 'hydriam' and
                name != 'Navale' and
                name != 'Vasak Desktop' and
                name != 'Hydriam')

    def get_windows_to_desktop(self):
        temp_list = []
        for win in self.get_windows():
            if (win.get_window_type() < 1 and
                    self.name_valid(win.get_class_instance_name())):
                datawin = {
                    "name": win.get_class_instance_name().replace("-", " "),
                    "id": win.get_xid(),
                    "icon": icons.get(win.get_class_instance_name())
                }
                temp_list.append(datawin)

        return json.dumps(temp_list)

    def get_windows(self):
        return self.get_screen().get_windows()

    @dbus.service.method('ar.net.vasak.os.desktop.service', in_signature='s', out_signature='')
    def toggle_window(self, id_window):
        for win in self.get_windows():
            if win.get_xid() == int(id_window):
                if win.is_minimized():
                    win.unminimize(datetime.timestamp(datetime.now()))
                else:
                    win.minimize()

    @dbus.service.method('ar.net.vasak.os.desktop.service', in_signature='', out_signature='s')
    def get_notifications(self):
        return str(self.notify.get_notifications())

    @dbus.service.method('ar.net.vasak.os.desktop.service', in_signature='s', out_signature='')
    def add_notification(self, noti):
        print(noti)
        self.notify.add_notification(json.loads(noti))
