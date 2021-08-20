import gi
import json
gi.require_version('Wnck', '3.0')
from gi.repository import Wnck
from datetime import datetime
import Lynx.Icons as icons


class LynxScreen:

    def __init__(self, dockDBus):
        self.minimized_windows = []
        self.dockdbus = dockDBus
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
        self.dockdbus.UpdateWindowsDock(windows)
        
    def nameValid(self, name):
        return (name != 'lynx-dock' and
                name != 'lynx-desktop')

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

        return(json.dumps(temp_list))

    def get_windows(self):
        return self.get_screen().get_windows()
    
    def toggleWindow(self, idWindow):
        for win in self.get_windows():
            if win.get_xid() == idWindow:
                if win.is_minimized():
                    win.unminimize(datetime.timestamp(datetime.now()))
                else:
                    win.minimize()

