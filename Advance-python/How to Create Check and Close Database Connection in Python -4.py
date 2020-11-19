import mysql.connector
config = {
    "user":"root",
    "password":"munna02",
    "host":"localhost",
    "port":3307 #3306
}
try:
    conn = mysql.connector.connect(**config)
except:
    print("Unable to connect!!")