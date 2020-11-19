#insert row from user input-tuple
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

sql = "INSERT INTO student_1(name,roll,fees) VALUES(%s,%s,%s)"
myc = conn.cursor(prepared=True)
name = input("Enter the name->>")
roll = int(input("Enter the roll->>"))
fees = float(input("Enter the fees->>"))
params = (name,roll,fees)
try:
    myc.execute(sql,params)
    conn.commit()
    print(myc.rowcount,"row inserted")
    print(f"Stu_ID->>{myc.lastrowid} inserted")
except:
    conn.rollback()
    print("Unable to insert data!!")

myc.close()
conn.close()