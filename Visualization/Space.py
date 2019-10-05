"""
Used by all the drones to communicate between all the drones near it
"""
import threading
import time
import socket
HOST = 'localhost'
PORT = 6666  # test port


class ServerThread(threading.Thread):
    def __init__(self, threadID, name, counter, *args):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.args = args

    def run(self):
        print("printing args")
        print(self.args)
        client(self, self.args[0], self.args[1])
        return


def client(self, client_socket, addr):
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
    SOCK.bind((HOST, PORT))
    SOCK.listen(5)


def main():
    threads = []

    for i in range(0, 5):
        client_sock, addr = SOCK.accept()
        print("Connected at: ", addr)
        args = []
        args.append(client_sock)
        args.append(addr)
        thread1 = ServerThread(1, "Thread 1", 1, args)
        thread1.start()
        threads.append(thread1)

    time.sleep(1)


if __name__ == "__main__":
    init()
    main()

