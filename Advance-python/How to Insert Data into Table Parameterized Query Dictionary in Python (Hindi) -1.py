import mysql.connector
try:
    conn = mysql.connector.connect(
        user="root",
        password="munna02",
        host="localhost",
        database = "pdb",
        port=3306
    )
    if (conn.is_connected()):
        print("Connected")
except:
    print("Unable to connect!!")

sql = "INSERT INTO student_1(name,roll,fees) VALUES(%(n)s, %(roll)s, %(fees)s)"
myc = conn.cursor()
try:
    myc.execute(sql,{"n":"Kona","roll":100035, "fees":2450.00})
    conn.commit()
    print(myc.rowcount,"row inserted.")
    print(f"STU_ID->>{myc.lastrowid} inserted.")
except:
    conn.rollback()
    print("Unaable to show data!!")

myc.close()
conn.close()