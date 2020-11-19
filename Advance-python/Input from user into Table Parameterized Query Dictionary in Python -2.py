#insert multiple rows-user input -dictionary
import mysql.connector
def student_data(nm,rl,fe):
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

    sql = "INSERT INTO student_1(name,roll,fees) VALUES(%(name)s, %(roll)s, %(fees)s)"
    myc = conn.cursor()
    params = {"name": nm, "roll": rl, "fees": fe}
    try:
        myc.execute(sql, params)
        conn.commit()
        print(myc.rowcount, "row inserted.")
        print(f"STU_ID->>{myc.lastrowid} inserted.")
    except:
        conn.rollback()
        print("Unaable to insert!!")

    myc.close()
    conn.close()

while True:
    nm = input("Enter the name->>")
    rl = input("Enter the roll->>")
    fe = float(input("Enter the fees->>"))
    student_data(nm,rl,fe)
    ans = input("Do you want exit??(y/n)")
    if (ans=="y"):
        break

