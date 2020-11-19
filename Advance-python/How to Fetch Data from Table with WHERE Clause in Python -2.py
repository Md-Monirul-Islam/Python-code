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

sql = "SELECT * FROM student WHERE stuid=5"
myc = conn.cursor()
try:
    myc.execute(sql)
    row = myc.fetchone()
    stuid = row[0]
    name = row[1]
    roll = row[2]
    fees = row[3]
    print(f"Stu_ID->>{stuid} Name->>{name} Roll->>{roll} Fees->>{fees}")
    print(myc.rowcount,"row counted")
except:
    conn.rollback()
    print("Unaable to show data!!")

myc.close()
conn.close()