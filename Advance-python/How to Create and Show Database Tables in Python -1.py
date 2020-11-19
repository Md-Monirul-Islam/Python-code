import mysql.connector
try:
    conn = mysql.connector.connect(
    user="root",
    password="munna02",
    host="localhost",
    database="pdb",
    port=3306
   )
    if(conn.is_connected()):
        print("Connected")
except:
    print("Unable to connect!!")

sql = "CREATE TABLE student_1(stuid INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(20), roll INT, fees FLOAT)"
myc = conn.cursor()
myc.execute(sql)
myc.close()
conn.close()