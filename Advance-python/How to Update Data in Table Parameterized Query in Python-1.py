#update data
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

sql = "UPDATE student_1 SET fees=%s WHERE stuid=%s"
myc = conn.cursor()
#update_value = (32.50.50,14)

try:
    myc.execute(sql,(3250.50,14))   #(sql,update_value)
    conn.commit()
    print(myc.rowcount, "row updated.")

except:
    conn.rollback()
    print("Unable to update!!")

myc.close()
conn.close()