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

sql = "DELETE FROM student_1 WHERE stuid=%s"
myc = conn.cursor(prepared=True)
params = (1,)
try:
    myc.execute(sql,params)
    conn.commit()
    print(myc.rowcount,"row deleted")
    print(f"Stu_ID->>{myc.lastrowid} deleted")
except:
    conn.rollback()
    print("Unable to delete data!!")

myc.close()
conn.close()