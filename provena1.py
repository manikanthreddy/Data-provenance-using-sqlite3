#This program gets two values from a DB into lineEdits.
import sys
import os
from provenA import *
from PyQt5 import QtWidgets, QtGui, QtCore

class MyForm(QtWidgets.QMainWindow):
  def __init__(self,parent=None):
     QtWidgets.QWidget.__init__(self,parent)
     self.ui = Ui_MainWindow()
     self.ui.setupUi(self)
     self.ui.pushButton.clicked.connect(self.updcust)
     self.ui.pushButton_2.clicked.connect(self.crcsv)
     self.ui.pushButton_3.clicked.connect(self.admn1)
     self.ui.pushButton_5.clicked.connect(self.cdetails)
     self.ui.pushButton_6.clicked.connect(self.admn3)
     self.ui.pushButton_7.clicked.connect(self.admn2)
     self.ui.pushButton_8.clicked.connect(self.admn4)
     

  def updcust(self):
    os.system("python customerupd1.py")

  def crcsv(self):
    os.system("python createcsv1.py")

  def admn1(self):
    os.system("python admin1.py")

  def cdetails(self):
    os.system("python customer1.py")
	
  def admn3(self):
    os.system("python admin3.py")

  def admn2(self):
    os.system("python admin2.py")
	
  def admn4(self):
    os.system("python admin4.py")


          
if __name__ == "__main__":  
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
