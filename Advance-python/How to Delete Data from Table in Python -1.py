#delete row
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

sql = "DELETE FROM student WHERE stuid=10"
myc = conn.cursor()
try:
    myc.execute(sql)
    conn.commit()
    print(myc.rowcount,"row deleted.")
except:
    conn.rollback()
    print("not deletable row!!")

myc.close()
conn.close()