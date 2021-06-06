import socket

host = 'localhost'
port = 8080

print("Client Running")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))

#1024 in bytes
message = sock.recv(1024)


while message:
    print("Here is what the server says:", message.decode())
    message=sock.recv(1024)

sock.close()