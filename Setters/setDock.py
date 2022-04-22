import gi
import sys
gi.require_version('Wnck', '3.0')
gi.require_version("Gtk", "3.0")
from gi.repository import Wnck, Gtk, Gdk
import Xlib
from Xlib.display import Display
from Xlib import X

screen = Wnck.Screen.get_default()
screen.force_update()
temp_windows = screen.get_windows()

for win in temp_windows:
  if (str(win.get_pid()) == sys.argv[1] or win.get_class_instance_name() == 'lynx-dock'):
    display = Display()
    topw = display.create_resource_object('window', win.get_xid())
    
    win.set_window_type(2)
    win.set_skip_tasklist(true)
    win.set_skip_pager(true)
    win.stick()
    win.make_above()
    win.unshade()
    print(win.get_xid())

    topw.change_property(display.intern_atom('_NET_WM_STRUT'),
                       display.intern_atom('CARDINAL'), 32,
                       [0, 0, 34, 0 ],
                       ## [0, 0, 0, 34 ], Para Bottom
                       X.PropModeReplace)
    topw.change_property(display.intern_atom('_NET_WM_STRUT_PARTIAL'),
                       display.intern_atom('CARDINAL'), 32,
                       [0, 0, 34, 0, 0, 0, 0, 0, 0, int(sys.argv[2])-1, 0, 0],
                       ## [0, 0, 34, 0, 0, 0, 0, 0, 0, 0, 0, int(sys.argv[2])-1], Para bottom
                       X.PropModeReplace)

