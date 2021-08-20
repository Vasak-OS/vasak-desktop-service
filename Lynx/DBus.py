import dbus
import dbus.service as service

def client(busName):
    bus = dbus.SessionBus()
    service = bus.get_object(busName, f"/{busName.replace('.', '/')}")
    return dbus.Interface(service, dbus_interface=busName)

class Service(dbus.service.Object):

    def __init__(self, screenParam, notifyParam):
        self.screen = screenParam
        self.notify = notifyParam
        bus_name = service.BusName("ar.net.lynx.os.desktop.service", dbus.SessionBus())
        service.Object.__init__(self, bus_name, "/ar/net/lynx/os/desktop/service")

    @dbus.service.method("ar.net.lynx.os.desktop.service", in_signature='s', out_signature='')
    def toggleWindow(self, idWindow):
        self.screen.toggleWindow(int(idWindow))
    
    @dbus.service.method("ar.net.lynx.os.desktop.service", in_signature='', out_signature='s')
    def getNotifications(self):
        return self.notify.getNotifications()