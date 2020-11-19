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

sql = "SELECT * FROM student WHERE name='Monirul'"
myc = conn.cursor()
try:
    myc.execute(sql)
    row = myc.fetchone()
    while row is not None:
        print(row)
        row = myc.fetchone()
    print(myc.rowcount,"row counted")
except:
    conn.rollback()
    print("Unaable to show data!!")

myc.close()
conn.close()