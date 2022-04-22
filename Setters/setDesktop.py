import gi
gi.require_version('Wnck', '3.0')
from gi.repository import Wnck

screen = Wnck.Screen.get_default()
screen.force_update()
temp_windows = screen.get_windows()

for win in temp_windows:
  if (str(win.get_pid()) == sys.argv[1] or win.get_class_instance_name() == 'lynx-desktop'):
    win.set_window_type(1)
    win.pin()
    win.make_below()
    win.set_skip_tasklist(true)
    win.set_skip_pager(true)
    win.unshade()
