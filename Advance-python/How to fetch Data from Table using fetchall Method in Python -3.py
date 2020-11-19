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

sql = "SELECT * FROM student"
myc = conn.cursor()
try:
    myc.execute(sql)
    rows = myc.fetchall()
    for i in rows:
        stuid = i[0]
        name = i[1]
        roll = i[2]
        fees = i[3]
        print(f"Sud_ID->>{stuid} Name->>{name} Roll->>{roll} Fess->>{fees}")
        print()
    print("Total rows->>",myc.rowcount)
except:
    conn.rollback()
    print("Unable to show data!!")

myc.close()
conn.close()