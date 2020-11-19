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

sql = "UPDATE student_1 SET fees=%s WHERE stuid=%s"
myc = conn.cursor(prepared=True)
id = int(input("Enter the student id->>"))
fe = float(input("Enter the fees->>"))
update_value = (id,fe)
try:
    myc.execute(sql,update_value)
    conn.commit()
    print("row update")
    #print(f"Stu_ID->>{myc.lastrowid} update")
except:
    conn.rollback()
    print("Unable to update data!!")

myc.close()
conn.close()