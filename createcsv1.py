#Note: After the .csv is crested,open it in notepad++, and remove the gaps between lines
import sys
import csv
import os

import sqlite3
con = sqlite3.connect('proven1')

cur = con.cursor()
cur.execute('SELECT * FROM log;')
rows = cur.fetchall()
fp = open('log1.csv', 'w')
myFile = csv.writer(fp)
myFile.writerows(rows)
fp.close()
print('log1.csv file successfully created')
con.commit()

