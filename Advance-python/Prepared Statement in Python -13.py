#retrive data-user input
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

sql = "SELECT * FROM student_1 WHERE stuid=%s"   #stuid=%s or stuid=?
myc = conn.cursor(prepared=True)
n= int(input("Enter the Student_ID->>"))
params = (n,)
try:
    myc.execute(sql,params)
    row = myc.fetchone()
    print(row)
    print(f"Total rows->>",myc.rowcount)
except:
    conn.rollback()
    print("Unable to retrive data!!")

myc.close()
conn.close()