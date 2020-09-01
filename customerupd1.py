import sys
from customerupd import *
from PyQt5 import QtWidgets, QtGui, QtCore
import os

import sqlite3
con = sqlite3.connect('proven1')

#import MySQLdb as mdb
#con = mdb.connect('localhost', 'team1', 'test623', 'drless1'); 

class MyForm(QtWidgets.QMainWindow):
  def __init__(self,parent=None):
     QtWidgets.QWidget.__init__(self,parent)
     self.ui = Ui_MainWindow()
     self.ui.setupUi(self)
     self.ui.pushButton_2.clicked.connect(self.updvalues)
     self.ui.pushButton.clicked.connect(self.getvalues)

  def updvalues(self):
    with con:
      cur = con.cursor()
      aadhar = str(self.ui.lineEdit.text())
      cid = str(self.ui.lineEdit_3.text())
      cname = str(self.ui.lineEdit_4.text())
      addr1 = str(self.ui.lineEdit_5.text())
      addr2 = str(self.ui.lineEdit_6.text())	
      mobile = str(self.ui.lineEdit_2.text())
      cur.execute('UPDATE customer SET cid=?,cname=?,addr1=?,addr2=?,aadharid=?,mobileid=?',(cid,cname,addr1,addr2,aadhar,mobile))
      con.commit()
      print("Details successfully updated in customer entity")
      os.system("python change1.py")
	  
  def getvalues(self):
    with con:
      cur = con.cursor()
      cid1 = str(self.ui.lineEdit_3.text())
      cur.execute('select cname,addr1,addr2,aadharid,mobileid from customer where cid = ?',[cid1])
      record = cur.fetchone()
        #print(record)
      self.ui.lineEdit_4.setText(record[0])
      self.ui.lineEdit_5.setText(record[1])
      self.ui.lineEdit_6.setText(record[2])
      self.ui.lineEdit.setText(record[3])
      self.ui.lineEdit_2.setText(record[4])
        
if __name__ == "__main__":  
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
