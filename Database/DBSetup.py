import mysql.connector
import uuid

mydb = mysql.connector.connect(
    host="localhost",
    user="Bois",
    passwd="HackUpstate",
    database="drones",
    auth_plugin="mysql_native_password"
)


def main():
    c = mydb.cursor()
    createTable(c)

    pass


def createTable(c):
    sql = "CREATE TABLE drones(id char(32) PRIMARY KEY, " \
          "droneType INT, " \
          "listenPort INT)"

    sql2 = "CREATE TABLE dronesLocation(id char(32) PRIMARY KEY, " \
           " locX DOUBLE(8,4) NOT NULL," \
           " locY DOUBLE(8,4) NOT NULL," \
           " locZ DOUBLE(8,4) NOT NULL," \
           " dirX DOUBLE(8,4) NOT NULL," \
           " dirY DOUBLE(8,4) NOT NULL," \
           " dirZ DOUBLE(8,4) NOT NULL)"

    c.execute(sql)
    c.execute(sql2)
    mydb.commit()



if __name__ == "__main__":
    main()