#update data
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

sql = "UPDATE student SET fees=10000 WHERE stuid=15"
myc = conn.cursor()
try:
    myc.execute(sql)
    conn.commit()
    print(myc.rowcount,"row updated")
except:
    conn.rollback()
    print("Unable to update!!")

myc.close()
conn.close()