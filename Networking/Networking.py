"""
File name: Networking.py
Author: Kyle Ferguson ~ krf6081@rit.edu
Date created: 10/05/2019
Date last modified: 10/05/2019
Python Version: 3.7

The networking framework for our drones.  Middleman for the drones and the field.
"""

import socket  # for sockets
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
    Returns a socket which is tied to the server.
    Drone holds this socket in a variable for future communication.
    :return:
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


def drone_send_info(s, message):
    """
    Sends a message to the server
    :param s: the socket on which the drone is connected to the server
    :param message: the message to be sent
    :return: success status (None == success)
    """
    return s.sendall(str.encode(str(message)))


def main():
    s1 = drone_connect()
    s2 = drone_connect()
    s3 = drone_connect()
    print(drone_send_info(s1, "drone 1 checking in"))
    print(drone_send_info(s2, "drone 2 checking in"))
    print(drone_send_info(s3, "drone 3 checking in"))
    print(s1.getsockname())
    print(s2.getsockname())
    print(s3.getsockname())


if __name__ == '__main__':
    main()
