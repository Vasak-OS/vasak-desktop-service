class Notifications:

  def __init__(self):
    self.notificationsList = []

  def addNotification(self,noti):
    self.notificationsList.append(noti)
    print(self.notificationsList)
  
  def getNotifications(self):
    return self.notificationsList
