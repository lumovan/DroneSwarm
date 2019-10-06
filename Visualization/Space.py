"""
Used by all the drones to communicate between all the drones near it
"""
import socket
import pickle
import time
from threading import Lock, Thread
from Drones.Drone import DroneData
from Database.DBHelper import *
from Database.connection import mydb

TCP_IP = "192.168.137.5"
TCP_PORT = 6666
BUFFER_SIZE = 1024

FIELDDIM = 1000
lock = Lock()


class ServerThread(Thread):
    def __init__(self, ip, port, conn):
        Thread.__init__(self)
        self.ip = ip
        self.conn = conn
        self.port = port
        self.db = DBHelper(mydb, mydb.cursor())

        print("New socket thread started for " + ip + ":" + str(port))

    def run(self):
        id = ""
        currLoc = ()

        # get initial drone location
        while True:
            data = self.conn.recv(200)
            if data:
                data = pickle.loads(data)
                if isinstance(data, DroneData):
                    print("Server Received Initial: ", data.position, "\tvel: ", data.velocity, "\tName: ", data.name)
                    currLoc = data.position
                    id = data.name
                    lock.acquire()
                    self.db.addDrone(data.name, data.position, data.velocity)
                    lock.release()
                break
            else:
                break

        # continuously update position and send neighbors
        while True:
            # send Neighbors
            self.sendNeighborghs(id, currLoc)
            # print("sent Neighbors")

            # receive next location
            while True:
                data = self.conn.recv(1024)
                if data:
                    data = pickle.loads(data)
                    if isinstance(data, DroneData):
                        currLoc = data.position
                        # print("Server Received New Position: ", data.position, "\tvel: ", data.velocity, "\tName: ", data.name)
                        lock.acquire()
                        self.db.update(data.name, data.position, data.velocity)
                        lock.release()
                        break

    def sendNeighborghs(self, id, location):
        # droneList = getLocalDronesSphere(id, location)
        lock.acquire()
        # droneList = self.db.getLocalDronesSquare(id, location)
        droneList = self.db.getLocalDronesSphere(id, location)
        lock.release()

        numDrones = len(droneList)
        # print(numDrones)

        self.conn.sendall(str.encode(str(numDrones)))

        # check to see
        if numDrones > 0:
            while True:
                data = self.conn.recv(20)
                if data:
                    break

            data = pickle.dumps(droneList, protocol=pickle.HIGHEST_PROTOCOL)
            self.conn.sendall(data)





def main():
    tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    tcpServer.bind((TCP_IP, TCP_PORT))
    threads = []

    cursor = mydb.cursor()
    clearTables(mydb, cursor)

    while True:
        tcpServer.listen(4)
        (conn, (ip, port)) = tcpServer.accept()

        newthread = ServerThread(ip, port, conn)
        newthread.start()
        threads.append(newthread)

    for t in threads:
        t.join()


if __name__ == "__main__":
    main()