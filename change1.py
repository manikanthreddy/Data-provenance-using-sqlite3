import sys
import os
from change import *
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
     with con:
    
        cur = con.cursor()
        cur.execute('SELECT chdesc FROM change;');
        result = cur.fetchall()
        for row in result:
            (self.ui.comboBox.addItem(row[0]))
     self.ui.pushButton.clicked.connect(self.updn)			

  def updn(self):
    with con:
      cur = con.cursor()
      selection = str(self.ui.comboBox.currentText())
      cid = str(self.ui.lineEdit_3.text())
      uid = str(self.ui.lineEdit_4.text())
      if (uid[0] == 'A'): utype = 'A'
      else: utype = 'U'
      if (selection[0] == 'D'): chngid = '1'
      else: chngid = '2'
      cur.execute('INSERT INTO log VALUES(?,?,?,?)',(uid,utype,chngid,cid))
    con.commit()
        
if __name__ == "__main__":  
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
