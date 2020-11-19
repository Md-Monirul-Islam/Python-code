#close()
import mysql.connector
dir = {
    "user":"root",
    "password":"munna02",
    "host":"localhost",       #optional
    "port":3306               #optional
}
try:
    conn = mysql.connector.connect(**dir)
    if(conn.is_connected()):
        print("Connected")
except:
    print("Unable to connect!!")
print("Before close->>",conn.is_connected())
conn.close()
print("After colse->>",conn.is_connected())