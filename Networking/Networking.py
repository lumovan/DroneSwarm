"""
File name: Networking.py
Author: Kyle Ferguson ~ krf6081@rit.edu
Date created: 10/05/2019
Date last modified: 10/06/2019
Python Version: 3.7

The networking framework for our drones.  Middleman for the drones and the field.
Drone data is transported to and from the server by pickling DroneData objects.
    (Pickling involves translating an object into binary data that can be sent through the socket)
"""

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
    Connects a drone to the server (Drone holds onto returned socket for future communication)
    :return: the socket which is tied to the server
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as err:
        print("socket creation failed with error %s" % err)
    s.connect((fieldIP, fieldPort))
    return s


def drone_disconnect(s):
    """
    Disconnects a drone from the server
    :param s: the socket through which the drone is connected to the server
    :return:
    """
    s.shutdown()
    s.close()


def drone_send_info(s, data):
    """
    Sends a drone data object to the server
    :param s: the socket through which the drone is connected to the server
    :param data: the data to be sent
    :return: success status (None == success)
    """
    protocol = pickle.HIGHEST_PROTOCOL
    data_string = pickle.dumps(data, protocol)
    return s.sendall(data_string)


def drone_receive_info(s):
    """
    Receives neighbor information from the Space server in two steps:
        1) receives number of drones data classes being sent in step 2 (the number of neighbors around the drone)
        2) receives a list of neighbors
    :param s: the socket through which the drone is connected to the server
    :return: the list of neighbors (as DroneData objects) - None means no neighbors or error
    """
    number_string = s.recv(50)  # Step 1 ~ received initially as a string
    number = -1
    if number_string:
        number = int(number_string)
        if number == 0:  # if no neighbors, skip the rest of the process
            return None
        s.sendall(str.encode(str(1)))  # send a confirmation to server that number was received ~ message means nothing
    else:
        print("NO NUMBER RECEIVED")
        return None

    drone_list_pickled = s.recv(number * 200)  # Step 2
    if drone_list_pickled:
        drone_list = pickle.loads(drone_list_pickled)  # unpickling the list from binary data back to a list
        if isinstance(drone_list, list):
            return drone_list
        else:
            print("DID NOT RECEIVE A LIST IN THE PICKLE, MARK!")
            return None
