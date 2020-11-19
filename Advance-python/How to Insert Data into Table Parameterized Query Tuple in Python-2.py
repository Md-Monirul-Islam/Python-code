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
sql = "INSERT INTO student_1(name,roll,fees) VALUES(%s, %s, %s)"
params = ("Monir",115167,3250.50)
myc = conn.cursor()

try:
    myc.execute(sql,params)
    conn.commit()
    print(myc.rowcount,"row inserted")
    print(f"Stu_ID:{myc.lastrowid} inserted")
except:
    conn.rollback()
    print("Unable to insert data")

myc.close()
conn.close()