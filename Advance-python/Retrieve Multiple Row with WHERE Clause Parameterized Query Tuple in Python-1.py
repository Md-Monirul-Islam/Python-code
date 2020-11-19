#retrive multiple row with clause
#from user input
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

sql = "SELECT * FROM student_1 WHERE fees=%s"
myc = conn.cursor()
#n = int(input("Enter the Student_ID->>"))
fetch_value = (3250.50,)
try:
    myc.execute(sql,fetch_value)
    row = myc.fetchone()
    while row is not None:
        print(row)
        row = myc.fetchone()
    print("Total rows",myc.rowcount)
except:
    conn.rollback()
    print("Unable to fecth data!!")
myc.close()
conn.close()