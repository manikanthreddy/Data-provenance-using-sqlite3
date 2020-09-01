import sys
from customer import *
from PyQt5 import QtWidgets, QtGui, QtCore

import sqlite3
con = sqlite3.connect('proven1')

#import MySQLdb as mdb
#con = mdb.connect('localhost', 'team1', 'test623', 'drless1'); 

class MyForm(QtWidgets.QMainWindow):
  def __init__(self,parent=None):
     QtWidgets.QWidget.__init__(self,parent)
     self.ui = Ui_MainWindow()
     self.ui.setupUi(self)
     self.ui.pushButton.clicked.connect(self.insertvalues)

  def insertvalues(self):
    with con:
      cur = con.cursor()
      aadhar = str(self.ui.lineEdit.text())
      cid = str(self.ui.lineEdit_3.text())
      cname = str(self.ui.lineEdit_4.text())
      addr1 = str(self.ui.lineEdit_5.text())
      addr2 = str(self.ui.lineEdit_6.text())	
      mobile = str(self.ui.lineEdit_2.text())
      cur.execute('INSERT INTO customer VALUES(?,?,?,?,?,?)',(cid,cname,addr1,addr2,aadhar,mobile))
      con.commit()
        
if __name__ == "__main__":  
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
