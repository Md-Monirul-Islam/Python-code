#insert data from user input using loop

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
    myc = conn.cursor()
    name = Name
    roll = Roll
    fees = Fees
    params = (name,roll,fees)

    try:
        myc.execute(sql,params)
        conn.commit()
        print(myc.rowcount)
        print(f"STU_ID->>{myc.lastrowid} inserted.")
    except:
        conn.rollback()
        print("Unable to connect!!")

    myc.close()
    conn.close()

while True:
    Name = input("Enter the name->>")
    Roll = input("Enter the roll->>")
    Fees = float(input("Enter the fees->>"))
    student_data(Name,Roll,Fees)
    ans = input("Do you want exit?(y/n)")  #y = yes,,n = no
    if (ans=="y"):
        break