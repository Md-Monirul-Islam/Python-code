#dictionary
#user input
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

sql = "DELETE FROM student_1 WHERE stuid=%(id)s"
myc = conn.cursor()
#n = input("Enter the row number->>")
#dl_row = {"id":12}

try:
    myc.execute(sql, {"id":12})   #sql,dl_row
    conn.commit()
    print(myc.rowcount, "row deleted.")

except:
    conn.rollback()
    print("Unaable to delete!!!!")

myc.close()
conn.close()