"""
Used by all the drones to communicate between all the drones near it
"""
import socket
import pickle
from threading import Thread
from Drones.Drone import DroneData

TCP_IP = "192.168.137.5"
TCP_PORT = 6666
BUFFER_SIZE = 1024


class ServerThread(Thread):
    def __init__(self, ip, port):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        print("New socket thread started for " + ip + ":" + str(port))

    def run(self):
        while True:
            data = conn.recv(200)
            if data:
                data = pickle.loads(data)
                if isinstance(data, DroneData):
                    print("Better Received Position: ", data.position, "\tvel: ", data.velocity, "\tName: ", data.name)
                print("Server Received: ", data)
            else:
                break


tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpServer.bind((TCP_IP, TCP_PORT))
threads = []

while True:
    tcpServer.listen(4)
    (conn, (ip, port)) = tcpServer.accept()
    newthread = ServerThread(ip, port)
    newthread.start()
    threads.append(newthread)



for t in threads:
    t.join()