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


    def __init__(self):
        c = mydb.cursor()
        global c

    def getLocalDrones(self, droneLocation):
        pass

    def updatePosVel(self, droneID, dronePos, droneVel):
        pass

    def addDrone(self, droneID, dronePos, droneVel):
        sql = "INSERT INTO drones(id,  droneType, listenPort) VALUE({}, 0, 0)".format(droneID)      # enter into drones table
        sql2 = "INSERT INTO droneslocation(id, locX, locY, locZ) VALUE({}, {}, {}, {})".format(
            droneID, dronePos[0], dronePos[1], dronePos[2])
        sql3 = "INSERT INTO dronesVel(id, locX, locY, locZ) VALUE({}, {}, {}, {})".format(
            droneID, droneVel[0], droneVel[1], droneVel[2])
        c.execute(sql)
        c.execute(sql2)
        c.execute(sql3)
        mydb.commit()

    def clearTables(self):
        c.execute("TRUNCATE TABLE drones")
        mydb.commit()
