#update data
import mysql.connector
def student_data(nm,rl,fe,id):
    try:
        conn = mysql.connector.connect(
            user="root",
            password="munna02",
            host="localhost",
            database="pdb",
            port=3306
        )
        if conn.is_connected():
            print("connected")
    except:
        print("Unable to connect!!")

    sql = "UPDATE student_1 SET name=%s, roll=%s, fees=%s WHERE stuid=%s"
    myc = conn.cursor(prepared=True)
    nm = name
    rl = roll
    fe = fees
    id = id
    seq_of_params = (nm,rl,fe,id)
    try:
        myc.execute(sql,seq_of_params)
        conn.commit()
        print("Row updated")
    except:
        conn.rollback()
        print("Unable o update data!!")
    myc.close()
    conn.close()

while True:
    name = input("Enter the name->>")
    roll = int(input("Enter the roll->>"))
    fees = float(input("Enter the fees->>"))
    id = int(input("Enter the Student_ID->>"))
    student_data(name,roll,fees,id)
    ans = input("Do you want to exit?(y/n)")
    if ans=="y":
        break
