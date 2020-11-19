#retrive all rows
import mysql.connector
try:
    conn = mysql.connector.connect(
        user="root",
        password="munna02",
        host="localhost",
        database="pdb",
        port=3306
    )
    if (conn.is_connected()):
        print("Connected")
except:
    print("Unable to connect!!")

sql = "SELECT name FROM student"
myc = conn.cursor()
try:
    myc.execute(sql)
    rows = myc.fetchall()
    for i in rows:
        print(i)
        print()
    print("Total rows->>",myc.rowcount)
except:
    conn.rollback()
    print("Unable to show data!!")

myc.close()
conn.close()