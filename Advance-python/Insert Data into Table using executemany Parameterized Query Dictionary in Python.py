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

sql = "INSERT INTO student_1(name,roll,fees) VALUES(%(name)s, %(roll)s, %(fees)s)"
myc = conn.cursor()
params = [
    {"name":"Rasel_2","roll":100045, "fees":2400.00},
    {"name":"Bipul","roll":100050,"fees":2400.00},
    {"name":"Sakil","roll":100055,"fees":2400.00}
]
try:
    myc.executemany(sql,params)
    conn.commit()
    print(myc.rowcount,"row inserted.")
    print(f"STU_ID->>{myc.lastrowid} inserted.")
except:
    conn.rollback()
    print("Unaable to show data!!")

myc.close()
conn.close()