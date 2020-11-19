import mysql.connector
try:
    conn = mysql.connector.connect(
    user="root",
    password="munna02",
    host="localhost",
    port=3306
)
    if (conn.is_connected()):
        print("Connected")
except:
    print("Unable to connected!!")

sql = "SHOW DATABASES"
myc = conn.cursor()
myc.execute(sql)
for d in myc:
    print(d)

myc.close()
conn.close()