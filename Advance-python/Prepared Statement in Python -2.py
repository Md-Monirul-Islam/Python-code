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

sql = "INSERT INTO student_1(name,roll,fees) VALUES(?,?,?)"
myc = conn.cursor(prepared=True)
params = ("Shohan",117744,2550.00)
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