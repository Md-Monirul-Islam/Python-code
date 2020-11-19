#insert data from user input using loop
import mysql.connector
def student_data(n,r,f):
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
    n = name
    r = roll
    f = fees
    params = (n,r,f)

    try:
        myc.execute(sql, params)
        conn.commit()
        print(myc.rowcount, "row inserted")
        print(f"STU_ID->>{myc.lastrowid} inserted.")

    except:
        conn.rollback()
        print("Unable to insert data!!")

    myc.close()
    conn.close()

while True:
    name = input("Enter the name->>")
    roll = input("Enter the roll->>")
    fees = float(input("Enter the fees->>"))
    student_data(name,roll,fees)
    ans = input("DO you want to exit??(yes/no)")
    if ans == "yes":
        break

