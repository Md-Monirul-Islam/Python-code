#Row count proverty
#multiple row insert
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

slq = "INSERT INTO student(name,roll,fees) VALUES ('Moni',10190,501.30), " \
      "('Sabbir',1231,984.909),('Fahim',1292,902.90)"
myc = conn.cursor()
try:
    myc.execute(slq)
    conn.commit()
    print(myc.rowcount,"Rows inserted.")
except:
    conn.rollback()
    print("Insertable row")

myc.close()
conn.close()