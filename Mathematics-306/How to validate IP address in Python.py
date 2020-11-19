import socket
ip_address = "103.139.9.211"
try:
    socket.inet_aton(ip_address)
    print("Valid IP.")
except socket.error:
    print("Invalid IP.")
