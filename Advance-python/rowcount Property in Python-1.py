#Row count proverty
#single row
import mysql.connector
try:
    conn = mysql.connector.connect(
        user="root",
        password="munna02",
        host="localhost",
        database="pdb",
        port=3306
    )
    if conn.is_connected():
        print("Connected")
except:
    print("Unable to connect!!")

slq = "INSERT INTO student(name,roll,fees) VALUES ('Monir',1010,201.30)"
myc = conn.cursor()
try:
    myc.execute(slq)
    conn.commit()
    print(myc.rowcount,"Row inserted.")
except:
    conn.rollback()
    print("Insertable row")

myc.close()
conn.close()