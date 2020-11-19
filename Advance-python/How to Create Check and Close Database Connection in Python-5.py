import mysql.connector
dir = {
    "user":"root",
    "password":"munna02",
    "host":"localhost",
    "port":3300  #3306
}
try:
    conn = mysql.connector.connect(**dir)
    print(conn.is_connected())
except:
    print("Unable to connect!!")