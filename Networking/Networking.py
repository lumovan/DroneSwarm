"""
File name: Networking.py
Author: Kyle Ferguson ~ krf6081@rit.edu
Date created: 10/05/2019
Date last modified: 10/05/2019
Python Version: 3.7

The networking framework for our drones.  Middleman for the drones and the field.
"""

from Drones.Drone import DroneData #for testing REMOVE LATER
import socket  # for sockets
import pickle  # for sending drone data to server
from time import sleep

# # # # # # # # # # # # # # # # # # Networking Thoughts Box # # # # # # # # # # # # # # # # # # # # #
# Drones need to:                                                                                   #
#   -connect with the field -> send ID, position, velocity                                          #
#       -then send new position new velocity, request to the field for locations of close drones    #
#       -accept array list of drone locations from field                                            #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


fieldIP = '192.168.137.5' #1036.252.145 209.217.218.34
fieldPort = 6666


def drone_connect():
    """
    Connects a drone to the server
    :return: the socket which is tied to the server
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Socket successfully created")
    except socket.error as err:
        print("socket creation failed with error %s" % err)
    s.connect((fieldIP, fieldPort))
    print("connected to " + fieldIP)
    return s


def drone_send_info(s, data):
    """
    Sends a drone data object to the server
    :param s: the socket on which the drone is connected to the server
    :param data: the data to be sent
    :return: success status (None == success)
    """
    data_string = pickle.dumps(data)
    return s.send(data_string)


# def main():
#     dronelist = []
#     for i in range(1):
#         dronelist.append(drone_connect())
# 
#     for i in range(10):
#         data = DroneData()
#         data.id = ""
#         num = 0.0
#         data.position = (num, num, num)
#         data.velocity = (num, num, num)
#         print(drone_send_info(dronelist[0], data))
#         # sleep(1)
#     dronelist[0].close

    # print(drone_send_info(s2, "drone 2 checking in"))
    # s2.close()
    # print(drone_send_info(s3, "drone 3 checking in"))
    # s3.close()


# if __name__ == '__main__':
#     main()
