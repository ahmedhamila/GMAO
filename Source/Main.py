from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import sys
from Views.LogIn import Ui_Dialog as LogIn
class Main:
    def __init__(self) -> None:
        self.window=QDialog()
        self.ui=LogIn()
        self.ui.setupUi(self.window)
        self.window.show()    


app=QtWidgets.QApplication(sys.argv)
window=Main()
app.exec_()