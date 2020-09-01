import sys
import os
from provenu import *
from PyQt5 import QtWidgets, QtGui, QtCore

class MyForm(QtWidgets.QMainWindow):
  def __init__(self,parent=None):
     QtWidgets.QWidget.__init__(self,parent)
     self.ui = Ui_MainWindow()
     self.ui.setupUi(self)
     self.ui.pushButton.clicked.connect(self.updcust)
     self.ui.pushButton_5.clicked.connect(self.cdetails)
     

  def updcust(self):
    os.system("python customerupd1.py")

  def cdetails(self):
    os.system("python customer1.py")
          
if __name__ == "__main__":  
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
