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

sql = "SELECT * FROM student"
myc = conn.cursor()

try:
    myc.execute(sql)
    row = myc.fetchone()
    while row is not None:
        stuid = row[0]
        name = row[1]
        roll = row[2]
        fees = row[3]
        print(f"Stud ID->>{stuid} Name->>{name} Roll->>{roll} Fess->>{fees}")
        print()
        row = myc.fetchone()
    print("Total rows->>",myc.rowcount)
except:
    conn.rollback()
    print("Unable to show data!!")

myc.close()
conn.close()