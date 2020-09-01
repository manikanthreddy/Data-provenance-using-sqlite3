import sys
import os
from login import *
from PyQt5 import QtWidgets, QtGui, QtCore
#import pymysql
#con = pymysql.connect(host='localhost', port=3306, user='team1', passwd='test623', db='pgrank1') 
import sqlite3
con = sqlite3.connect('proven1')

class MyForm(QtWidgets.QMainWindow):
  def __init__(self,parent=None):
     QtWidgets.QWidget.__init__(self,parent)
     self.ui = Ui_MainWindow()
     self.ui.setupUi(self)
     self.ui.pushButton.clicked.connect(self.registn)
     self.ui.pushButton_2.clicked.connect(self.logn)

  

  def registn(self):
         os.system("python register1.py")

  def logn(self):
    
     with con:
    
        cur = con.cursor()
        uname = str(self.ui.lineEdit_4.text())
        pwd1 = str(self.ui.lineEdit_5.text())
        cur.execute('select passwd from user where uname = ?',[uname])
        record = cur.fetchone()
        print(record)
        if (record[0] == pwd1): 
          print("Login Credentials Matched")
          if (uname[0] == 'A'): os.system("python provena1.py")
          else: os.system("python provenu1.py")
        else: 
          print("Login Credentials Not Matched")
        con.commit()
        
if __name__ == "__main__":  
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
