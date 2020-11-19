#insert multiple row
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

sql = "INSERT INTO student(name,roll,fees) VALUES('Monirul',1155165,3200.50)," \
      "('Swapan',115178,3200.60),('Habib',180121,3032.45)"
myc = conn.cursor()
try:
    myc.execute(sql)
    conn.commit()
    print("Row inserted")
except:
    conn.rollback()
    print("Row not insertable!!")

myc.close()
conn.close()
