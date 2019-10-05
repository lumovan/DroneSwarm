"""
File name: Networking.py
Author: Kyle Ferguson ~ krf6081@rit.edu
Date created: 10/05/2019
Date last modified: 10/05/2019
Python Version: 3.7

The networking framework for our drones.  Middleman for the drones and the field.
"""

import socket  # for sockets

# # # # # # # # # # # # # # # # # # Networking Thoughts Box # # # # # # # # # # # # # # # # # # # # #
# Drones need to:                                                                                   #
#   -connect with the field -> send ID, position, velocity                                          #
#       -then send new position new velocity, request to the field for locations of close drones    #
#       -accept array list of drone locations from field                                            #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
fieldIP = '192.168.137.13' #1036.252.145 209.217.218.34
fieldPort = 6666


def drone_connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((fieldIP, fieldPort))
    print("connected")
    return s


def main():
    s = drone_connect()
    s.sendall(str.encode("*Notices your bulge* OwO"))
    data = s.recv(1024)  # same buffsize
    print(str(data))


if __name__ == '__main__':
    main()
