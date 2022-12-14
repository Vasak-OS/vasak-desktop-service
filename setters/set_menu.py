from gi.repository import Wnck
import gi
import sys
gi.require_version('Wnck', '3.0')

screen = Wnck.Screen.get_default()
screen.force_update()
temp_windows = screen.get_windows()

for win in temp_windows:
    if (str(win.get_pid()) == sys.argv[1] or
        win.get_class_instance_name() == 'hydriam' or
            win.get_class_instance_name() == 'Hydriam'):
        win.set_window_type(5)
        win.set_skip_tasklist(True)
        win.set_skip_pager(True)
        win.unshade()
