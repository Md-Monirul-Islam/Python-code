#insert single row
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
sql = 'INSERT INTO student(name,roll,fees) VALUES("Munna",180126,3200.50)'
myc = conn.cursor()
myc.execute(sql)
conn.commit()
myc.close()
conn.close()