#lastrowid
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
    print("Unable to connect")

sql = "INSERT INTO student(name,roll,fees) VALUES ('Sultan',180109,3200.50), " \
      "('Kalam',12903,1239.90), ('Rabin',111290,3250.50)"
myc = conn.cursor()
try:
    myc.execute(sql)
    conn.commit()
    print(myc.lastrowid)
except:
    conn.rollback()
    print("Not insertable row!!")

myc.close()
conn.close()