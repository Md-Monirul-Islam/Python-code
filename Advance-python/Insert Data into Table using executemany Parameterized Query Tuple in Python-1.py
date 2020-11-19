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
myc = conn.cursor()
seq_of_params = [("naim",113186,3250.50), ("Ashik",115176,3250.50), ("Ahsan",115136,3250.50)]

try:
    myc.executemany(sql,seq_of_params)
    conn.commit()
    print(myc.rowcount,"row inserted")

except:
    conn.rollback()
    print("Unable to insert data")

myc.close()
conn.close()