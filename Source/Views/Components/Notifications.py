from PyQt5 import QtCore
import time
from Services.NotificationServices import getNotifications,getDemandeInterventionUntreated
from datetime import datetime, timedelta
import QNotifications
import qtpy
import notifypy
class NotificationThread(QtCore.QThread):
    def __init__(self,matricule_RM) -> None:
        super().__init__()
        self.matricule_RM=matricule_RM
    update_notif=QtCore.pyqtSignal(str)
    def run(self):
        self.update_notif.emit("NonTraitee")
        while True:
            
            status,rec = getNotifications(self.matricule_RM,'DemandeIntervention')
            
            print("Checking Notifs")
            for r in rec :
                timeNow = datetime.time(datetime.now())
                timeBefore1Min = datetime.time(datetime.now()-timedelta(minutes=1))
                print(timeNow)
                print("---",datetime.time(r[3]))
                print(timeBefore1Min)
                if timeBefore1Min<=datetime.time(r[3]) <=timeNow : 
                    self.update_notif.emit("Notification")
            print("Sleeping ...")
            time.sleep(25)
class Notification(QtCore.QObject) :
    notify = qtpy.QtCore.Signal(
		['QString', 'QString', int, bool],
		['QString', 'QString', int, bool, 'QString']
	)
    
    def __init__(self,notification_area,matricule) -> None:
        super(Notification,self).__init__()
        self.notification_area_Object=notification_area
        self.notification_area=self.__setup_notification_area(self.notification_area_Object)
        self.matricule=matricule
        
    def start_Thread(self,matricule):
        self.worker=NotificationThread(matricule)
        self.worker.start()
        self.worker.update_notif.connect(self.updateNotif)
    
    def updateNotif(self,type):
        if(type == "Notification"):
            self.__submit_message()
            self.sendDesktopNotification("Nouvelle Notification","Vous avez une nouvelle notification, Check your notifications Tab ","GMAO")
        else:
            status,rec = getDemandeInterventionUntreated(self.matricule)
            if status :
                self.__submit_message("Vous avez "+str(len(rec))+" notifications non traitées !","danger")
                self.sendDesktopNotification("Notification","Vous avez "+str(len(rec))+" notification non Traitée ","GMAO")
    
    
    def __submit_message(self,textvalue="Vous avez une nouvelle notification",typevalue="primary",duration=5000,autohide=False,entryeffect="fadeIn",exiteffect="fadeOut",entryduration=500,exitduration=500,buttontext="OK"):
        if textvalue:
            if entryeffect != "None":
                self.notification_area.setEntryEffect(entryeffect,
                    entryduration)
            else:
                self.notification_area.setEntryEffect(None)
            if exiteffect != "None":
                self.notification_area.setExitEffect(exiteffect,
                    exitduration)
            else:
                self.notification_area.setExitEffect(None)
            if buttontext:
                self.notify['QString', 'QString', int, bool, 'QString'].emit(
                    textvalue, typevalue, duration, autohide, buttontext
                )
            else:
                self.notify['QString', 'QString', int, bool].emit(
                    textvalue, typevalue, duration, autohide
                )    
    def sendDesktopNotification(self,title,message,application_name):
        notification=notifypy.Notify()
        notification.title=title
        notification.message=message
        notification.application_name=application_name
        notification.icon="./Views/Components/notification.png"
        notification.send()
        
    def __setup_notification_area(self, targetWidget):
        notification_area = QNotifications.QNotificationArea(targetWidget)
        self.notify['QString', 'QString', int, bool].connect(
            notification_area.display
        )
        self.notify['QString', 'QString', int, bool, 'QString'].connect(
            notification_area.display
        )
        return notification_area