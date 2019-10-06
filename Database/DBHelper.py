import mysql.connector
from Drones.Drone import DroneData

# mydb = mysql.connector.connect(
#     host="localhost",
#     user="Bois",
#     passwd="HackUpstate",
#     database="drones",
#     auth_plugin="mysql_native_password"
# )

# from Database.connection import mydb

ViewDistance = 100


class DBHelper:
    def __init__(self, mydb, c):
        self.mydb = mydb
        self.c = c

    def getLocalDronesSquare(self, droneID, droneLocation):
        droneID = "\"" + droneID + "\""
        sql = "SELECT id, locX, locY, locZ, dirX, dirY, dirZ FROM droneslocation WHERE " \
              "locX <= {} AND locX >= {} AND " \
              "locY <= {} AND locY >= {} AND " \
              "locZ <= {} AND locZ >= {} AND id != {}"\
            .format(droneLocation[0] + ViewDistance, droneLocation[0] - ViewDistance,
                     droneLocation[1] + ViewDistance, droneLocation[1] - ViewDistance,
                     droneLocation[2] + ViewDistance, droneLocation[2] - ViewDistance,
                    droneID)

        self.c.execute(sql)

        neighbors = []
        for tb in self.c:
            neighbors.append(DroneData(tb[4:7], tb[1:4], tb[0]))
        # print(neighbors)
        return neighbors

    def getLocalDronesSphere(self, droneID, droneLocation):
        droneID = "\"" + droneID + "\""
        sql = "SELECT id, locX, locY, locZ, dirX, dirY, dirZ FROM droneslocation WHERE " \
              "POWER({} - locX, 2) + " \
              "POWER({} - locY, 2) + " \
              "POWER({} - locZ, 2) <= " \
              "POWER({}, 2) AND id != {}"\
            .format(droneLocation[0], droneLocation[1], droneLocation[2], ViewDistance, droneID)

        self.c.execute(sql)

        neighbors = []
        for tb in self.c:
            neighbors.append(DroneData(tb[4:7], tb[1:4], tb[0]))
        # print(neighbors)
        return neighbors

    def getNumDrones(self):
        self.c.execute("SELECT id FROM drones")
        drones = self.c.fetchall()

        count = 0
        for cs in drones:
            count += 1
        return count

    def update(self, droneID, dronePos, droneVel):
        droneID = "\"" + droneID + "\""
        # sql = "UPDATE droneslocation SET locX = {}, locY = {}, locZ = {}, dirX = {}, dirY = {}, dirZ = {} WHERE id = {}".format(
        #     dronePos[0], dronePos[1], dronePos[2], droneVel[0], droneVel[1], droneVel[2], droneID)
        sql = "UPDATE droneslocation SET locX = {}, locY = {}, locZ = {} WHERE id = {}".format(
            dronePos[0], dronePos[1], dronePos[2], droneID)
        self.c.execute(sql)
        self.mydb.commit()

    def addDrone(self, droneID, dronePos, droneVel):
        droneID = "\"" + droneID + "\""
        sql = "INSERT INTO drones(id,  droneType, listenPort) VALUE({}, 0, 0)".format(droneID)      # enter into drones table
        sql2 = "INSERT INTO droneslocation(id, locX, locY, locZ, dirX, dirY, dirZ) VALUE({}, {}, {}, {}, {}, {}, {})".format(
            droneID, dronePos[0], dronePos[1], dronePos[2], droneVel[0], droneVel[1], droneVel[2])
        self.c.execute(sql)
        self.c.execute(sql2)
        self.mydb.commit()


def clearTables(mydb, c):
    c.execute("TRUNCATE TABLE drones")
    c.execute("TRUNCATE TABLE droneslocation")
    mydb.commit()
    print("Tables clearned")
