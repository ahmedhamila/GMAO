from PyQt5 import QtCore, QtGui, QtWidgets
from .. import icons_rc
from ..BonTravailViews.BonTravailList import Ui_Dialog as Bontravail_UI
from ..BonTravailViews.BonTravailConsulter import Ui_Dialog as BontravailConsulter_UI
from ..DemandeInterventionViews.DemandeInterventionList import Ui_Dialog as DemandeIntervention_UI
from ..DemandeInterventionViews.DemandeInterventionConsulter import Ui_Dialog as DemandeInterventionConsulter_UI
from ..EquipementViews.EquipementList import Ui_Dialog as Equipement_UI
from ..EquipementViews.EquipementConsulter import Ui_Dialog as EquipementConsulter_UI
from ..BonApprovisonnementViews.BonApprovisionnementList import Ui_Dialog as BonApprovisionment_UI
from ..BonApprovisonnementViews.BonApprovisionnementConsulter import Ui_Dialog as BonApprovisionmentConsulter_UI
from .ListeUser import Ui_Dialog as ListeUser2
from .Dashboard import Ui_Dialog as dashboard
from PyQt5.QtWidgets import *
from Services import ResponsableMaintenanceServices,ResponsableProductionServices,ResponsableChaineProductionServices,MagasinierServices

from .Dashboard import Ui_Dialog as Dashboard_UI
from ..Components.CollapsibleBox import CollapsibleBox



from ..Components.Notifications import NotificationThread,Notification
class Ui_MainWindow(QtCore.QObject):

    
    def __init__(self,matricule,role,dialogSignIn,window) -> None:
        super(Ui_MainWindow,self).__init__()
        self.matricule = matricule
        self.role = role
        self.dialogSignIn=dialogSignIn
        self.window=window
        self.NotificationObject=Notification(self.window,self.matricule)
    
    def slideLeftMenu(self,x):
        if x=="1":
            width=self.left_side_menu.width()
            if width ==75:
                    newwidth=285
            else:
                newwidth=75
            self.animation=QtCore.QPropertyAnimation(self.left_side_menu,b"minimumWidth")
            self.animation.setDuration(250)
            self.animation.setStartValue(width)
            self.animation.setEndValue(newwidth)
            self.animation.start()
        if x=="2":
            width=self.left_side_menu.width()
            if width ==75:
                    newwidth=285
                    self.animation=QtCore.QPropertyAnimation(self.left_side_menu,b"minimumWidth")
                    self.animation.setDuration(250)
                    self.animation.setStartValue(width)
                    self.animation.setEndValue(newwidth)
                    self.animation.start()
        if x=="3":
            width=self.left_side_menu.width()
            if width ==285:
                    newwidth=75
                    self.animation=QtCore.QPropertyAnimation(self.left_side_menu,b"minimumWidth")
                    self.animation.setDuration(250)
                    self.animation.setStartValue(width)
                    self.animation.setEndValue(newwidth)
                    self.animation.start()


    
        

    def handleadd(self):
        self.adduser = QtWidgets.QDialog()
        self.ui_adduser =ListeUser2(self.stackedWidget)
        self.ui_adduser.setupUi(self.adduser)
        self.stackedWidget.addWidget(self.adduser)
        self.stackedWidget.setCurrentWidget(self.adduser)

    def affdash(self):
        
        self.affda = QtWidgets.QDialog()
        self.ui_affda =dashboard()
        self.ui_affda.setupUi(self.affda)
        self.stackedWidget.addWidget(self.affda)
        self.stackedWidget.setCurrentWidget(self.affda)


    def displayBonTravail(self):
        self.dialogBonTravail = QtWidgets.QDialog()
        self.uiBonTravail = Bontravail_UI(self,self.dialogBonTravail)
        self.uiBonTravail.setupUi(self.dialogBonTravail)
        self.stackedWidget.addWidget(self.dialogBonTravail)
        self.stackedWidget.setCurrentWidget(self.dialogBonTravail)
    def displayDashboard(self):
        self.dialogDashboard = QtWidgets.QDialog()
        self.uiDashboard = Dashboard_UI()
        self.uiDashboard.setupUi(self.dialogDashboard)
        self.stackedWidget.addWidget(self.dialogDashboard)
        self.stackedWidget.setCurrentWidget(self.dialogDashboard)
    def displayBonTravailConsulter(self):
        self.dialogBonTravailConsulter = QtWidgets.QDialog()
        self.uiBonTravailConsulter = BontravailConsulter_UI(self)
        self.uiBonTravailConsulter.setupUi(self.dialogBonTravailConsulter)
        self.stackedWidget.addWidget(self.dialogBonTravailConsulter)
        self.stackedWidget.setCurrentWidget(self.dialogBonTravailConsulter)
    def displayEquipement(self):
        self.dialogEquipement = QtWidgets.QDialog()
        self.uiEquipement = Equipement_UI(self,self.dialogEquipement)
        self.uiEquipement.setupUi(self.dialogEquipement)
        self.stackedWidget.addWidget(self.dialogEquipement)
        self.stackedWidget.setCurrentWidget(self.dialogEquipement)
    def displayEquipementConsulter(self):
        self.dialogEquipementConsulter = QtWidgets.QDialog()
        self.uiEquipementConsulter = EquipementConsulter_UI(self)
        self.uiEquipementConsulter.setupUi(self.dialogEquipementConsulter)
        self.stackedWidget.addWidget(self.dialogEquipementConsulter)
        self.stackedWidget.setCurrentWidget(self.dialogEquipementConsulter)
    def displayBonApprovisionment(self):
        self.dialogBonApprovisionment = QtWidgets.QDialog()
        self.uiBonApprovisionment = BonApprovisionment_UI(self)
        self.uiBonApprovisionment.setupUi(self.dialogBonApprovisionment)
        self.stackedWidget.addWidget(self.dialogBonApprovisionment)
        self.stackedWidget.setCurrentWidget(self.dialogBonApprovisionment)
    def displayBonApprovisionmentConsulter(self):
        self.dialogBonApprovisionmentConsulter = QtWidgets.QDialog()
        self.uiBonApprovisionmentConsulter = BonApprovisionmentConsulter_UI()
        self.uiBonApprovisionmentConsulter.setupUi(self.dialogBonApprovisionmentConsulter)
        self.stackedWidget.addWidget(self.dialogBonApprovisionmentConsulter)
        self.stackedWidget.setCurrentWidget(self.dialogBonApprovisionmentConsulter)
    def displayDemandeIntervention(self):
        self.dialogDemandeIntervention = QtWidgets.QDialog()
        self.uiDemandeIntervention = DemandeIntervention_UI(self,self.dialogDemandeIntervention)
        self.uiDemandeIntervention.setupUi(self.dialogDemandeIntervention)
        self.stackedWidget.addWidget(self.dialogDemandeIntervention)
        self.stackedWidget.setCurrentWidget(self.dialogDemandeIntervention)
    def displayDemandeInterventionConsulter(self):
        self.dialogDemandeInterventionConsulter = QtWidgets.QDialog()
        self.uiDemandeInterventionConsulter = DemandeInterventionConsulter_UI(self,self.dialogDemandeInterventionConsulter)
        self.uiDemandeInterventionConsulter.setupUi(self.dialogDemandeInterventionConsulter)
        self.stackedWidget.addWidget(self.dialogDemandeInterventionConsulter)
        self.stackedWidget.setCurrentWidget(self.dialogDemandeInterventionConsulter)

    def signOut(self):
        self.dialogSignIn.show()
        self.mainwindow.hide()
    def initialiseRM(self):
        ##############################################################################################################################################################################
                                                                            # Responsable Maintenance #
        ##############################################################################################################################################################################

        if self.role == 'ResponsableMaintenance':

            status,record = ResponsableMaintenanceServices.getResponsableMaintenance(self.matricule)
            if status:
                self.nom=record[0][1]
                self.prenom=record[0][2]
            
            self.affdash()
            self.DashboardBox = QtWidgets.QPushButton(
            text="Dashboard", checkable=True, checked=False
        )

            

            self.DashboardBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.DashboardBox.setStyleSheet("background-image: url(:/icons/icons/dashboard.png);\n"
    "background-repeat: none;\n"
    "padding-left: 50px;\n"
    "width: 150px;\n"
    "font: 75 16pt 'Arial';\n"
    "height: 22px;\n"
    "font-weight : bold;\n"
    "background-position: center left;")

            self.DashboardBox.clicked.connect(self.displayDashboard)
            self.formLayout.addWidget(self.DashboardBox)

            self.DashboardBox.clicked.connect(self.affdash)
            self.DashboardBox.clicked.connect(lambda:self.slideLeftMenu("2"))

            self.MaintenanceBox = CollapsibleBox('Maintenance',self.left_menu_top_buttons,2,":/icons/icons/tools.png")
            lay = QtWidgets.QVBoxLayout()
            self.MaintenanceBox.toggle_button.pressed.connect(lambda:self.slideLeftMenu("2"))

            
            

            
            
            
        
            MaintenanceBonTravailPreventifCurative = QtWidgets.QPushButton("Bon de Travail")
            MaintenanceBonTravailPreventifCurative.clicked.connect(lambda:self.slideLeftMenu("3"))
            
            MaintenanceBonTravailPreventifCurative.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            MaintenanceBonTravailPreventifCurative.setStyleSheet("height : 17px ;font-weight:bold;")
            lay.addWidget(MaintenanceBonTravailPreventifCurative)
            
            MaintenanceBonTravailPreventifCurative.clicked.connect(self.displayBonTravail)
            
            self.MaintenanceBox.setContentLayout(lay)
            self.formLayout.addWidget(self.MaintenanceBox)


            
            self.NotificationsBox = CollapsibleBox('Notifications',self.left_menu_top_buttons,2,":/icons/icons/notification.png")
            self.NotificationsBox.toggle_button.pressed.connect(lambda:self.slideLeftMenu("2"))
            lay = QtWidgets.QVBoxLayout()
            NotificationsConsulterDemandesInterventions = QtWidgets.QPushButton("Demandes d'Interventions")
            NotificationsConsulterDemandesInterventions.clicked.connect(lambda:self.slideLeftMenu("3"))
            NotificationsConsulterDemandesInterventions.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            NotificationsConsulterDemandesInterventions.setStyleSheet("height : 17px ;font-weight:bold;")

            NotificationsConsulterDemandesInterventions.clicked.connect(self.displayDemandeInterventionConsulter)
            
            
            lay.addWidget(NotificationsConsulterDemandesInterventions)
            self.NotificationsBox.setContentLayout(lay)
            self.formLayout.addWidget(self.NotificationsBox)

            self.EquipementsBox = CollapsibleBox('Equipements',self.left_menu_top_buttons,2,":/icons/icons/truck.png")
            self.EquipementsBox.toggle_button.pressed.connect(lambda:self.slideLeftMenu("2"))
            lay = QtWidgets.QVBoxLayout()

            EquipementsConsulter = QtWidgets.QPushButton("Liste Équipements")
            EquipementsConsulter.clicked.connect(lambda:self.slideLeftMenu("3"))
            EquipementsConsulter.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            EquipementsConsulter.setStyleSheet("height : 17px ;font-weight:bold;")

            EquipementsConsulter.clicked.connect(self.displayEquipement)
            lay.addWidget(EquipementsConsulter)

            EquipementsDemandeApprovisionnement = QtWidgets.QPushButton("Demande d'Approvisionnement")
            EquipementsDemandeApprovisionnement.clicked.connect(lambda:self.slideLeftMenu("3"))
            EquipementsDemandeApprovisionnement.setStyleSheet("height : 17px ;font-weight:bold;")
            EquipementsDemandeApprovisionnement.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

            EquipementsDemandeApprovisionnement.clicked.connect(self.displayBonApprovisionment)
            lay.addWidget(EquipementsDemandeApprovisionnement)

            self.EquipementsBox.setContentLayout(lay)
            self.formLayout.addWidget(self.EquipementsBox)

            self.NotificationObject.start_Thread(self.matricule)
        ##############################################################################################################################################################################
    def initialiseRP(self):
        ##############################################################################################################################################################################
                                                                            # Responsable Production #
        ##############################################################################################################################################################################

        if self.role == 'ResponsableProduction':

            status,record = ResponsableProductionServices.getResponsableProduction(self.matricule)
            if status:
                self.nom=record[0][1]
                self.prenom=record[0][2]
            
            self.DashboardBox = QtWidgets.QPushButton(
            text="Dashboard", checkable=True, checked=False
        )
            self.DashboardBox.clicked.connect(lambda:self.slideLeftMenu("2"))
            self.DashboardBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.DashboardBox.setStyleSheet("background-image: url(:/icons/icons/dashboard.png);\n"
    "background-repeat: none;\n"
    "padding-left: 50px;\n"
    "width: 150px;\n"
    "font: 75 16pt 'Arial';\n"
    "height: 22px;\n"
    "font-weight : bold;\n"
    "background-position: center left;")
            self.formLayout.addWidget(self.DashboardBox)

            self.MaintenanceBox = CollapsibleBox('Maintenance',self.left_menu_top_buttons,2,":/icons/icons/tools.png")
            self.MaintenanceBox.toggle_button.pressed.connect(lambda:self.slideLeftMenu("2"))
            lay = QtWidgets.QVBoxLayout()
            
        
            MaintenanceBonTravailPreventif = QtWidgets.QPushButton("Bons de Travails")
            MaintenanceBonTravailPreventif.clicked.connect(lambda:self.slideLeftMenu("3"))
            MaintenanceBonTravailPreventif.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            MaintenanceBonTravailPreventif.setStyleSheet("height : 17px ;font-weight:bold;")
            lay.addWidget(MaintenanceBonTravailPreventif)

            MaintenanceBonTravailPreventif.clicked.connect(self.displayBonTravailConsulter)

            MaintenanceDemandesInterventions = QtWidgets.QPushButton("Demandes d'Interventions")
            MaintenanceDemandesInterventions.clicked.connect(lambda:self.slideLeftMenu("3"))
            MaintenanceDemandesInterventions.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            MaintenanceDemandesInterventions.setStyleSheet("height : 17px ;font-weight:bold;")
            lay.addWidget(MaintenanceDemandesInterventions)

            MaintenanceDemandesInterventions.clicked.connect(self.displayDemandeInterventionConsulter)
            
            self.MaintenanceBox.setContentLayout(lay)
            self.formLayout.addWidget(self.MaintenanceBox)


            


            self.UsersBox = CollapsibleBox('Utilisateurs',self.left_menu_top_buttons,2,":/icons/icons/group.png")
            self.UsersBox.toggle_button.pressed.connect(lambda:self.slideLeftMenu("2"))
            lay = QtWidgets.QVBoxLayout()

            UtilisateursConsulter = QtWidgets.QPushButton("Responsables Chaines-Productions")
            UtilisateursConsulter.clicked.connect(lambda:self.slideLeftMenu("3"))
            UtilisateursConsulter.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            UtilisateursConsulter.setStyleSheet("height : 17px ;font-weight:bold;")
            lay.addWidget(UtilisateursConsulter)


            self.UsersBox.setContentLayout(lay)
            self.formLayout.addWidget(self.UsersBox)


            self.EquipementsBox = CollapsibleBox('Equipements',self.left_menu_top_buttons,2,":/icons/icons/truck.png")
            self.EquipementsBox.toggle_button.pressed.connect(lambda:self.slideLeftMenu("2"))
            lay = QtWidgets.QVBoxLayout()

            EquipementsConsulter = QtWidgets.QPushButton("Liste Équipements")
            EquipementsConsulter.clicked.connect(lambda:self.slideLeftMenu("3"))
            EquipementsConsulter.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            EquipementsConsulter.setStyleSheet("height : 17px ;font-weight:bold;")
            lay.addWidget(EquipementsConsulter)

            EquipementsConsulter.clicked.connect(self.displayEquipementConsulter)

            EquipementsBonApprovisionnement = QtWidgets.QPushButton("Demandes d'Approvisionnements")
            EquipementsBonApprovisionnement.clicked.connect(lambda:self.slideLeftMenu("3"))
            EquipementsBonApprovisionnement.setStyleSheet("height : 17px ;font-weight:bold;")
            EquipementsBonApprovisionnement.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            lay.addWidget(EquipementsBonApprovisionnement)

            EquipementsBonApprovisionnement.clicked.connect(self.displayBonApprovisionmentConsulter)

            self.EquipementsBox.setContentLayout(lay)
            self.formLayout.addWidget(self.EquipementsBox)
        ##############################################################################################################################################################################
    def initialiseRCP(self):
        ##############################################################################################################################################################################
                                                                            # Responsable Chaine Production #
        ##############################################################################################################################################################################

        if self.role=="ResponsableChaineProduction":

            status,record = ResponsableChaineProductionServices.getResponsableChaineProduction(self.matricule)
            if status:
                self.nom=record[0][1]
                self.prenom=record[0][2]

            self.DashboardBox = QtWidgets.QPushButton(
            text="Dashboard", checkable=True, checked=False
        )
            self.DashboardBox.clicked.connect(lambda:self.slideLeftMenu("2"))
            self.DashboardBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.DashboardBox.setStyleSheet("background-image: url(:/icons/icons/dashboard.png);\n"
            "background-repeat: none;\n"
            "padding-left: 50px;\n"
            "font: 75 16pt 'Arial';\n"
            "width: 150px;\n"
            "height: 22px;\n"
            "font-weight: bold;\n"
            "background-position: center left;")
            self.formLayout.addWidget(self.DashboardBox)


            self.MaintenanceBox = CollapsibleBox('Maintenance',self.left_menu_top_buttons,1,":/icons/icons/tools.png")
            self.MaintenanceBox.toggle_button.pressed.connect(lambda:self.slideLeftMenu("2"))
            lay = QtWidgets.QVBoxLayout()

            MaintenanceDemandeIntervention = QtWidgets.QPushButton("Demandes d'Interventions")
            MaintenanceDemandeIntervention.clicked.connect(lambda:self.slideLeftMenu("3"))
            MaintenanceDemandeIntervention.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            MaintenanceDemandeIntervention.setStyleSheet("height: 17px;font-weight: bold;")
            lay.addWidget(MaintenanceDemandeIntervention)

            self.MaintenanceBox.setContentLayout(lay)
            self.formLayout.addWidget(self.MaintenanceBox)


            self.NotificationsBox = CollapsibleBox('Notifications',self.left_menu_top_buttons,1,":/icons/icons/notification.png")
            self.NotificationsBox.toggle_button.pressed.connect(lambda:self.slideLeftMenu("2"))
            lay = QtWidgets.QVBoxLayout()

            NotificationValidation = QtWidgets.QPushButton("Validation de Réception")
            NotificationValidation.clicked.connect(lambda:self.slideLeftMenu("3"))
            NotificationValidation.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            NotificationValidation.setStyleSheet("height: 17px;font-weight: bold;")
            lay.addWidget(NotificationValidation)

            self.NotificationsBox.setContentLayout(lay)
            self.formLayout.addWidget(self.NotificationsBox)


            self.EquipementsBox = CollapsibleBox('Equipements',self.left_menu_top_buttons,1,":/icons/icons/truck.png")
            self.EquipementsBox.toggle_button.pressed.connect(lambda:self.slideLeftMenu("2"))
            lay = QtWidgets.QVBoxLayout()

            ConsulterEquipement = QtWidgets.QPushButton("Liste Equipements")
            ConsulterEquipement.clicked.connect(lambda:self.slideLeftMenu("3"))
            ConsulterEquipement.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            ConsulterEquipement.setStyleSheet("height: 17px;font-weight: bold;")
            lay.addWidget(ConsulterEquipement)

            self.EquipementsBox.setContentLayout(lay)
            self.formLayout.addWidget(self.EquipementsBox)

            ConsulterEquipement.clicked.connect(self.displayEquipement)
            MaintenanceDemandeIntervention.clicked.connect(self.displayDemandeIntervention)
            








        ################################################################################################################################################################
    def initialiseAdmin(self):
        ###############################################################################################################################################################
                                                                    # Administrateur #
        ###############################################################################################################################################################


        if self.role=="Administrateur":

            '''status,record = ResponsableChaineProductionServices.getResponsableChaineProduction(self.matricule)
            if status:
                self.nom=record[0][1]
                self.prenom=record[0][2]'''
            self.nom=""
            self.prenom=""
            
            self.DashboardBox = QtWidgets.QPushButton(
            text="Dashboard", checkable=True, checked=False
        )
            self.DashboardBox.clicked.connect(lambda:self.slideLeftMenu("2"))
            self.DashboardBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.DashboardBox.setStyleSheet("background-image: url(:/icons/icons/dashboard.png);\n"
            "background-repeat: none;\n"
            "padding-left: 50px;\n"
            "font: 75 16pt 'Arial';\n"
            "width: 150px;\n"
            "font-weight: bold;\n"
            "height: 22px;\n"
            "background-position: center left;")

            self.DashboardBox.clicked.connect(self.displayDashboard)
            self.formLayout.addWidget(self.DashboardBox)


            self.MaintenanceBox = CollapsibleBox('Maintenance',self.left_menu_top_buttons,2,":/icons/icons/tools.png")
            self.MaintenanceBox.toggle_button.pressed.connect(lambda:self.slideLeftMenu("2"))
            lay = QtWidgets.QVBoxLayout()

        
            MaintenanceBonTravail = QtWidgets.QPushButton("Bons de Travails")
            MaintenanceBonTravail.clicked.connect(lambda:self.slideLeftMenu("3"))
            MaintenanceBonTravail.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            MaintenanceBonTravail.setStyleSheet("height: 17px;font-weight: bold;")
            lay.addWidget(MaintenanceBonTravail)

            MaintenanceBonTravail.clicked.connect(self.displayBonTravailConsulter)

            DemandeInterventioon = QtWidgets.QPushButton("Demande Interventions")
            DemandeInterventioon.clicked.connect(lambda:self.slideLeftMenu("3"))
            DemandeInterventioon.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            DemandeInterventioon.setStyleSheet("height: 17px;font-weight: bold;")
            lay.addWidget(DemandeInterventioon)

            DemandeInterventioon.clicked.connect(self.displayDemandeInterventionConsulter)
            
            self.MaintenanceBox.setContentLayout(lay)
            self.formLayout.addWidget(self.MaintenanceBox)



            self.UtilisateurBox = CollapsibleBox('Utilisateurs',self.left_menu_top_buttons,2,":/icons/icons/group.png")
            self.UtilisateurBox.toggle_button.pressed.connect(lambda:self.slideLeftMenu("2"))
            lay = QtWidgets.QVBoxLayout()

            CRUDUtilisateur = QtWidgets.QPushButton("Liste D'utilisateurs")
            CRUDUtilisateur.clicked.connect(lambda:self.slideLeftMenu("3"))
            CRUDUtilisateur.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            CRUDUtilisateur.setStyleSheet("height: 17px;font-weight: bold;")
            lay.addWidget(CRUDUtilisateur)

            self.UtilisateurBox.setContentLayout(lay)
            self.formLayout.addWidget(self.UtilisateurBox)


            self.EquipementsBox = CollapsibleBox('Equipements',self.left_menu_top_buttons,2,":/icons/icons/truck.png")
            self.EquipementsBox.toggle_button.pressed.connect(lambda:self.slideLeftMenu("2"))
            lay = QtWidgets.QVBoxLayout()

            ListeEquipement = QtWidgets.QPushButton("Liste d'Equipements")
            ListeEquipement.clicked.connect(lambda:self.slideLeftMenu("3"))
            ListeEquipement.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            ListeEquipement.setStyleSheet("height: 17px;font-weight: bold;")
            lay.addWidget(ListeEquipement)

            ListeEquipement.clicked.connect(self.displayEquipementConsulter)

            EquipementsDemandeApprovisionnement = QtWidgets.QPushButton("Demande d'Approvisionnements")
            EquipementsDemandeApprovisionnement.clicked.connect(lambda:self.slideLeftMenu("3"))
            EquipementsDemandeApprovisionnement.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            EquipementsDemandeApprovisionnement.setStyleSheet("height: 17px;font-weight: bold;")
            lay.addWidget(EquipementsDemandeApprovisionnement)

            EquipementsDemandeApprovisionnement.clicked.connect(self.displayBonApprovisionmentConsulter)


            self.EquipementsBox.setContentLayout(lay)
            self.formLayout.addWidget(self.EquipementsBox)

            CRUDUtilisateur.clicked.connect(self.handleadd)
    def initialiseMagasinier(self):
        ################################################################################################################
                                            #Magasiner
        #################################################################################################################
        if self.role=="Magasinier":

            status,record = MagasinierServices.getMagasinier(self.matricule)
            if status:
                self.nom=record[0][1]
                self.prenom=record[0][2]

                
            self.DashboardBox = QtWidgets.QPushButton(
            text="Dashboard", checkable=True, checked=False
        )
            self.DashboardBox.clicked.connect(lambda:self.slideLeftMenu("3"))
            self.DashboardBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.DashboardBox.setStyleSheet("background-image: url(:/icons/icons/dashboard.png);\n"
            "background-repeat: none;\n"
            "padding-left: 50px;\n"
            "font: 75 16pt 'Arial';\n"
            "width: 150px;\n"
            "font-weight: bold;\n"
            "height: 22px;\n"
            "background-position: center left;")
            self.formLayout.addWidget(self.DashboardBox)


            self.NotificationsBox = CollapsibleBox('Notifications',self.left_menu_top_buttons,1,":/icons/icons/notification.png")
            self.NotificationsBox.toggle_button.pressed.connect(lambda:self.slideLeftMenu("2"))
            lay = QtWidgets.QVBoxLayout()

            NotificationValidation = QtWidgets.QPushButton("Validation de Réception")
            NotificationValidation.clicked.connect(lambda:self.slideLeftMenu("3"))
            NotificationValidation.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            NotificationValidation.setStyleSheet("height: 17px;font-weight: bold;")
            lay.addWidget(NotificationValidation)

            self.NotificationsBox.setContentLayout(lay)
            self.formLayout.addWidget(self.NotificationsBox)


            self.EquipementsBox = CollapsibleBox('Equipements',self.left_menu_top_buttons,2,":/icons/icons/truck.png")
            self.EquipementsBox.toggle_button.pressed.connect(lambda:self.slideLeftMenu("2"))
            lay = QtWidgets.QVBoxLayout()

            ListeEquipement = QtWidgets.QPushButton("Liste Piéces de Rechanges")
            ListeEquipement.clicked.connect(lambda:self.slideLeftMenu("3"))
            ListeEquipement.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            ListeEquipement.setStyleSheet("height: 17px;font-weight: bold;")
            lay.addWidget(ListeEquipement)

            EquipementsDemandeApprovisionnement = QtWidgets.QPushButton("Demande d'Approvisionnements")
            EquipementsDemandeApprovisionnement.clicked.connect(lambda:self.slideLeftMenu("3"))
            EquipementsDemandeApprovisionnement.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            EquipementsDemandeApprovisionnement.setStyleSheet("height: 17px;font-weight: bold;")
            lay.addWidget(EquipementsDemandeApprovisionnement)


            self.EquipementsBox.setContentLayout(lay)
            self.formLayout.addWidget(self.EquipementsBox)



        ################################################################################################################
    def initialiseMainWindow(self):
        self.initialiseRM()
        self.initialiseRP()
        self.initialiseRCP()
        self.initialiseAdmin()
        self.initialiseMagasinier()
        self.LabesSpace.setText("Space "+self.role+"( "+self.matricule +" "+self.nom+" "+self.prenom+" )")
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1225, 717)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.main_header = QtWidgets.QFrame(self.centralwidget)
        self.main_header.setMaximumSize(QtCore.QSize(16777215, 50))
        self.main_header.setStyleSheet("QFrame{\n"
"    \n"
"    background-color: #22333B;\n"
"}")
        self.main_header.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.main_header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_header.setObjectName("main_header")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.main_header)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tittle_bar_container = QtWidgets.QFrame(self.main_header)
        self.tittle_bar_container.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tittle_bar_container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tittle_bar_container.setObjectName("tittle_bar_container")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.tittle_bar_container)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.left_menu_toggle = QtWidgets.QFrame(self.tittle_bar_container)
        self.left_menu_toggle.setMinimumSize(QtCore.QSize(50, 0))
        self.left_menu_toggle.setMaximumSize(QtCore.QSize(50, 16777215))
        self.left_menu_toggle.setStyleSheet("QFrame{\n"
"\n"
"}\n"
"QPushButton{\n"
"    padding: 5px 10px;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    background-color: #00A8E8;\n"
"    color: white;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(0, 92, 157);\n"
"}")
        self.left_menu_toggle.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.left_menu_toggle.setFrameShadow(QtWidgets.QFrame.Raised)
        self.left_menu_toggle.setObjectName("left_menu_toggle")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.left_menu_toggle)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.left_menu_toggle_btn = QtWidgets.QPushButton(self.left_menu_toggle)
        self.left_menu_toggle_btn.setMinimumSize(QtCore.QSize(0, 40))
        self.left_menu_toggle_btn.setMaximumSize(QtCore.QSize(50, 16777215))
        self.left_menu_toggle_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.left_menu_toggle_btn.setStyleSheet("background-image: url(:/icons/icons/menu.png);\n"
"background-repeat: none;\n"
"padding-left: 50px;\n"
"background-position: center ;")
        self.left_menu_toggle_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/cil-menu.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.left_menu_toggle_btn.setIcon(icon)
        self.left_menu_toggle_btn.setIconSize(QtCore.QSize(24, 24))
        self.left_menu_toggle_btn.setObjectName("left_menu_toggle_btn")
        self.horizontalLayout_4.addWidget(self.left_menu_toggle_btn)
        self.horizontalLayout_5.addWidget(self.left_menu_toggle)
        self.tittle_bar = QtWidgets.QFrame(self.tittle_bar_container)
        self.tittle_bar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tittle_bar.setStyleSheet("")
        self.tittle_bar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tittle_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tittle_bar.setObjectName("tittle_bar")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tittle_bar)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.LabesSpace = QtWidgets.QLabel(self.tittle_bar)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.LabesSpace.setFont(font)
        self.LabesSpace.setStyleSheet("color:white;")
        self.LabesSpace.setText("")
        self.LabesSpace.setAlignment(QtCore.Qt.AlignCenter)
        self.LabesSpace.setObjectName("LabesSpace")
        self.horizontalLayout_3.addWidget(self.LabesSpace)
        self.horizontalLayout_5.addWidget(self.tittle_bar)
        self.horizontalLayout_2.addWidget(self.tittle_bar_container)
        self.verticalLayout.addWidget(self.main_header)
        self.main_body = QtWidgets.QFrame(self.centralwidget)
        self.main_body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_body.setObjectName("main_body")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.main_body)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.left_side_menu = QtWidgets.QFrame(self.main_body)
        self.left_side_menu.setMaximumSize(QtCore.QSize(75, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.left_side_menu.setFont(font)
        self.left_side_menu.setStyleSheet("background-color: #22333B;")
        self.left_side_menu.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.left_side_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.left_side_menu.setObjectName("left_side_menu")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.left_side_menu)
        self.verticalLayout_3.setContentsMargins(7, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.scrollArea = QtWidgets.QScrollArea(self.left_side_menu)
        self.scrollArea.setStyleSheet("")
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.left_menu_top_buttons = QtWidgets.QWidget()
        self.left_menu_top_buttons.setGeometry(QtCore.QRect(0, 0, 66, 571))
        self.left_menu_top_buttons.setStyleSheet("QPushButton{\n"
"    padding: 20px 10px;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    background-color: #00A8E8;\n"
"    color: white;\n"
"    margin : 10px 5px; \n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(0, 92, 157);\n"
"}")
        self.left_menu_top_buttons.setObjectName("left_menu_top_buttons")
        self.formLayout = QtWidgets.QFormLayout(self.left_menu_top_buttons)
        self.formLayout.setObjectName("formLayout")
        self.scrollArea.setWidget(self.left_menu_top_buttons)
        self.verticalLayout_3.addWidget(self.scrollArea)
        self.SignOut = QtWidgets.QPushButton(self.left_side_menu)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.SignOut.setFont(font)
        self.SignOut.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.SignOut.setStyleSheet("\n"
"\n"
"QPushButton{\n"
"    padding: 20px 10px;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    background-color: #00A8E8;\n"
"    color: white;\n"
"    margin : 10px 5px; \n"
"    background-image: url(:/icons/icons/sign-out.png);\n"
"    background-repeat: none;\n"
"    padding-left: 50px;\n"
"    background-position: left center ;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(0, 92, 157);\n"
"}")
        self.SignOut.setObjectName("SignOut")
        self.verticalLayout_3.addWidget(self.SignOut)
        self.horizontalLayout.addWidget(self.left_side_menu)
        self.center_main_items = QtWidgets.QFrame(self.main_body)
        self.center_main_items.setStyleSheet("")
        self.center_main_items.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.center_main_items.setFrameShadow(QtWidgets.QFrame.Raised)
        self.center_main_items.setObjectName("center_main_items")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.center_main_items)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.stackedWidget = QtWidgets.QStackedWidget(self.center_main_items)
        self.stackedWidget.setStyleSheet("background-color: #FEFDFC;")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.verticalLayout_2.addWidget(self.stackedWidget)
        self.horizontalLayout.addWidget(self.center_main_items)
        self.verticalLayout.addWidget(self.main_body)
        self.main_footer = QtWidgets.QFrame(self.centralwidget)
        self.main_footer.setMaximumSize(QtCore.QSize(16777215, 30))
        self.main_footer.setStyleSheet("QFrame{\n"
"    background-color: grey;\n"
"}")
        self.main_footer.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.main_footer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_footer.setObjectName("main_footer")
        self.verticalLayout.addWidget(self.main_footer)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.mainwindow=MainWindow
        self.initialiseMainWindow()
        self.left_menu_toggle_btn.clicked.connect(lambda:self.slideLeftMenu("1"))
        self.SignOut.clicked.connect(self.signOut)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.SignOut.setText(_translate("MainWindow", "Sign Out"))
