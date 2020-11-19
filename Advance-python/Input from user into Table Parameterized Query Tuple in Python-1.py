#single row insert-input from user
import mysql.connector
try:
    conn = mysql.connector.connect(
        user="root",
        password="munna02",
        host="localhost",
        database="pdb",
        port=3306
    )
    if conn.is_connected():
        print("Connected")
except:
    print("Unabel to connect!!")

sql = "INSERT INTO student_1(name,roll,fees) VALUES(%s,%s,%s)"
myc = conn.cursor()
Name = input("Enter the name->>")
Roll = input("Enter the roll->>")
Fees = float(input("Enter the fees->>"))
params = (Name,Roll,Fees)

try:
    myc.execute(sql,params)
    conn.commit()
    print(myc.rowcount,"row inserted")
    print(f"STU_ID->>{myc.lastrowid} inserted.")

except:
    conn.rollback()
    print("Unable to insert data!!")

myc.close()
conn.close()