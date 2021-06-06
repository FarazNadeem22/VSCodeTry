import socket

host = 'localhost'
port = 8080


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host,port))

##Listen to one request at a time
sock.listen(1) 

## This returns 1. connection where the request comes from and the address 
con, address = sock.accept()

message = "Important Info Enclosed"

## encode and sent the message 
conn.send(message.encode())
conn.close()
