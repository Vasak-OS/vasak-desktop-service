class Notifications:

    def __init__(self):
        self.notifications_list = []

    def add_notification(self, noti):
        self.notifications_list.append(noti)
        print(self.notifications_list)

    def get_notifications(self):
        return self.notifications_list
