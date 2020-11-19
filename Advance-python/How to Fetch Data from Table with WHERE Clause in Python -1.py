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
    print(row)
    print(myc.rowcount,"row counted")
except:
    conn.rollback()
    print("Unaable to show data!!")

myc.close()
conn.close()