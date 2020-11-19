import mysql.connector
try:
    conn = mysql.connector.connect(
        user="root",
        password="munna0",
        host="localhost",
        port=3306
    )
except:
    print("Unable to connect!!!!")