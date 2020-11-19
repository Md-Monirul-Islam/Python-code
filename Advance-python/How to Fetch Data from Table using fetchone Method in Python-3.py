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
sql = "SELECT name, fees FROM student"
myc = conn.cursor()
try:
    myc.execute(sql)
    row = myc.fetchone()
    while row is not None:
        print(row)
        row = myc.fetchone()
    print("Total name->>",myc.rowcount)
except:
    conn.rollback()
    print("Unable to show data!!")

myc.close()
conn.close()