import mysql.connector
from Drones.Drone import DroneData

# mydb = mysql.connector.connect(
#     host="localhost",
#     user="Bois",
#     passwd="HackUpstate",
#     database="drones",
#     auth_plugin="mysql_native_password"
# )

from Database.connection import mydb


class DBHelper:
    def __init__(self):
        self.c = mydb.cursor()
        self.ViewDistance = 100

    def getLocalDrones(self, droneID, droneLocation):
        droneID = "\"" + droneID + "\""
        sql = "SELECT id, locX, locY, locZ, dirX, dirY, dirZ FROM droneslocation WHERE " \
              "locX <= {} AND locX >= {} AND " \
              "locY <= {} AND locY >= {} AND " \
              "locZ <= {} AND locZ >= {} AND id != {}"\
            .format(droneLocation[0] + self.ViewDistance, droneLocation[0] - self.ViewDistance,
                     droneLocation[1] + self.ViewDistance, droneLocation[1] - self.ViewDistance,
                     droneLocation[2] + self.ViewDistance, droneLocation[2] - self.ViewDistance,
                    droneID)

        self.c.execute(sql)

        neighbors = []
        for tb in self.c:
            neighbors.append(DroneData(tb[0], tb[1:4], tb[4:7]))
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
        sql = "UPDATE droneslocation SET locX = {}, locY = {}, locZ = {}, dirX = {}, dirY = {}, dirZ = {} WHERE id = {}".format(
            dronePos[0], dronePos[1], dronePos[2], droneVel[0], droneVel[1], droneVel[2], droneID)
        self.c.execute(sql)
        mydb.commit()

    def addDrone(self, droneID, dronePos, droneVel):
        droneID = "\"" + droneID + "\""
        sql = "INSERT INTO drones(id,  droneType, listenPort) VALUE({}, 0, 0)".format(droneID)      # enter into drones table
        sql2 = "INSERT INTO droneslocation(id, locX, locY, locZ, dirX, dirY, dirZ) VALUE({}, {}, {}, {}, {}, {}, {})".format(
            droneID, dronePos[0], dronePos[1], dronePos[2], droneVel[0], droneVel[1], droneVel[2])
        self.c.execute(sql)
        self.c.execute(sql2)
        mydb.commit()

    def clearTables(self):
        self.c.execute("TRUNCATE TABLE drones")
        mydb.commit()
