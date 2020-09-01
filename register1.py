#This program gets two values from a DB into lineEdits.
import sys
import os
from register import *
from PyQt5 import QtWidgets, QtGui, QtCore
import sqlite3

con = sqlite3.connect('proven1')

class MyForm(QtWidgets.QMainWindow):
  def __init__(self,parent=None):
     QtWidgets.QWidget.__init__(self,parent)
     self.ui = Ui_MainWindow()
     self.ui.setupUi(self)
     self.ui.pushButton_2.clicked.connect(self.insertvalues)
   

  def insertvalues(self):
         
     with con:
    
        cur = con.cursor()
        uname = str(self.ui.lineEdit_4.text())
        userid = str(self.ui.lineEdit_7.text())
        if (userid[0] == 'A'): utype = 'A'
        else: utype = 'U'
        mobino = str(self.ui.lineEdit_8.text())
        pwd1 = str(self.ui.lineEdit_5.text())
        pwd2 = str(self.ui.lineEdit_6.text())
        mailid = str(self.ui.lineEdit_9.text())        
        if (pwd1 != pwd2):
            print('re-typed password not matching')
        else:
            cur.execute('INSERT INTO user VALUES(?,?,?,?,?,?)',(uname,userid,utype,pwd1,mobino,mailid))
        con.commit()
	      
if __name__ == "__main__":  
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())



	
