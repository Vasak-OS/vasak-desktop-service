class Notifications:

  def __init__(self):
    self.notificationsList = []
    self.nextID = 0

  def addNotification(self,noti):
    self.notificationsList.append(noti)
    print(self.notificationsList)
  
  def getNotifications(self):
    return self.notificationsList
  
  def getNetxID(self):
    self.nextID += 1
    return self.nextID