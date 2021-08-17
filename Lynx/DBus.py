import dbus
import dbus.service as service

def client(busName):
    bus = dbus.SessionBus()
    service = bus.get_object(busName, f"/{busName.replace('.', '/')}")
    return dbus.Interface(service, dbus_interface=busName)

class Service(dbus.service.Object):

    def __init__(self):
        bus_name = service.BusName("ar.net.lynx.os.service", dbus.SessionBus())
        service.Object.__init__(self, bus_name, "/ar/net/lynx/os/service")

    @dbus.service.method("ar.net.lynx.os.service", in_signature='', out_signature='')
    def toggleLauncher(self):
        print(1)

    @dbus.service.method("ar.net.lynx.os.service", in_signature='', out_signature='')
    def screenToggle(self):
        print(1)
    