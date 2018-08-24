import sqlite3
# Create Database


#Data Definition Language

try:
    conn = sqlite3.connect('atm.db',timeout=10)
    obj=conn.execute('''CREATE TABLE  customerdetails(cardno REAL , pinno REAL, balance REAL,date TEXT);''')
    ob=conn.execute('''CREATE TABLE  cust(cardno REAL, pinno REAL, balance REAL,date TEXT);''')

except sqlite3.Error as e:
    print(e)
finally:
    conn.close()