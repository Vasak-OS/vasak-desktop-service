import dbus

def client(busName):
    bus = dbus.SessionBus()
    service = bus.get_object(busName, f"/{busName.replace('.', '/')}")
    return dbus.Interface(service, dbus_interface=busName)
