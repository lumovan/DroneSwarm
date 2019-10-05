"""
Used by all the drones to communicate between all the drones near it
"""
import socket
import threading
import time


def client(client_socket, addr):
    print("Client thread started")
    run = True
    while run:
        data = client_socket.recv(1024)
        if not data:
            run = False
            break
        client_socket.send(data)
    client_socket.close()


def init():
    global SOCK
    SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SOCK.bind(('192.168.137.5', 6666))
    SOCK.listen(5)


def main():
    client_sock, addr = SOCK.accept()
    for i in range(0, 5):
        print("Connected at: ", addr)
        print(client_sock.recv(1024))
    time.sleep(1)


if __name__ == '__main__':
    init()
    main()