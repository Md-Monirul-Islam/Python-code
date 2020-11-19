#insert multiple row from user input-tuple
import mysql.connector
def student_data(name,roll,fees):
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
    name = name
    roll = roll
    fees = fees

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

while True:
    name = input("Enter the name->>")
    roll = int(input("Enter the roll->>"))
    fees = float(input("Enter the fees->>"))
    studebt_data = (name,roll,fees)
    ans = input("Do you want to exit?(y/n)")
    if ans=="y":
        break