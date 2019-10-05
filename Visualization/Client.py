import socket

HOST = 'localhost'
PORT = 6666

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(str.encode('Hello, world'))
    data = s.recv(1024) # same buffsize

print('Recieved: ', str(data))

