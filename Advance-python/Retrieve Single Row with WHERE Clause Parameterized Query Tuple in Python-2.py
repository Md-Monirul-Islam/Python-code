#retrive single row with clause
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

sql = "SELECT * FROM student_1 WHERE stuid=%s"
myc = conn.cursor()
fetch_value = (7,)
try:
    myc.execute(sql,fetch_value)
    row = myc.fetchone()
    print(row)
    print("Total rows",myc.rowcount)
except:
    conn.rollback()
    print("Unable to fecth data!!")
myc.close()
conn.close()