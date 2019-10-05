import mysql.connector

# mydb = mysql.connector.connect(
#     host="localhost",
#     user="Bois",
#     passwd="HackUpstate",
#     database="drones",
#     auth_plugin="mysql_native_password"
# )

from Database.connection import mydb

class DBHelper:

    ViewDistance = 50

    def __init__(self):
        c = mydb.cursor()
        global c

    def getLocalDrones(self, droneLocation):
        pass

    def getNumDrones(self):
        c.execute("SELECT id FROM drones")
        drones = c.fetchall()

        count = 0
        for cs in drones:
            count += 1
        return count

    def setPosVel(self, droneID, dronePos, droneVel):
        sql = "UPDATE droneslocation SET locX = {}, locY = {}, locZ = {} WHERE id = {}".format(
            dronePos[0], dronePos[1], dronePos[2], droneID)
        sql2 = "UPDATE dronesdirection SET dirX = {}, dirY = {}, dirZ = {} WHERE id = {}".format(
            droneID, droneVel[0], droneVel[1], droneVel[2], droneID)
        c.execute(sql)
        c.execute(sql2)
        mydb.commit()

    def addDrone(self, droneID, dronePos, droneVel):
        sql = "INSERT INTO drones(id,  droneType, listenPort) VALUE({}, 0, 0)".format(droneID)      # enter into drones table
        sql2 = "INSERT INTO droneslocation(id, locX, locY, locZ) VALUE({}, {}, {}, {})".format(
            droneID, dronePos[0], dronePos[1], dronePos[2])
        sql3 = "INSERT INTO dronesdirection(id, , dirX, dirY, dirZ) VALUE({}, {}, {}, {})".format(
            droneID, droneVel[0], droneVel[1], droneVel[2])
        c.execute(sql)
        c.execute(sql2)
        c.execute(sql3)
        mydb.commit()

    def clearTables(self):
        c.execute("TRUNCATE TABLE drones")
        mydb.commit()
