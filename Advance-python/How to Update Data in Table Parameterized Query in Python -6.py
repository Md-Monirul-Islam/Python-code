#input from user
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

sql = "UPDATE student_1 SET name=%s, roll=%s, fees=%s WHERE stuid=%s"
myc = conn.cursor()
id = input(input("Enter stu_id to update->>"))
nm = input(input("Enter the name->>"))
ro = input(input("Enter the roll->>"))
fe = float(input("Enter the fees->>"))
update_value = (nm,ro,fe,id)
try:
    myc.execute(sql,update_value)
    conn.commit()
    print(myc.rowcount,"row updated")
except:
    conn.rollback()
    print("Unable to update_value!!")

myc.close()
conn.close()