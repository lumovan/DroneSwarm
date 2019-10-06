"""
File name: Drone.py
Author: Jacob Colley ~ jac9748@rit.edu
        Mark Takatsuka ~ mrt9583@rit.edu
        Kyle Feguson ~ krf6081@rit.edu
Date created: 10/05/2019
Date last modified: 10/06/2019
Python Version: 3.7

This file contains the classes for the drone objects and the data objects that are sent to the server.
"""
from Networking.Networking import *
from time import sleep
from threading import Thread, Lock
import uuid

# global variable for the maximum acceleration a drone can do
MAX_ACCEL = 50
MIN_DISTANCE = 5
FIELDDIM = 1000


class DroneData:
    """
    DroneData packages the drone's velocity, position, and name together for ease of sending to the Space server
    """
    def __init__(self, velocity, position, name):
        self.velocity = velocity
        self.position = position
        self.name = name


class Drone(Thread):
    """
    Drone contains functionality for drone movement and keeps track of the following fields:
        - Data ~ an instance of DroneData that keeps track of velocity, position,
            and the name of this drone (a unique identifier generated upon drone creation)
        - Socket ~ the connection this drone has to the Space server
        - Neighbors ~ a list of drones within the drone's view distance that the drone uses to position and move itself
    """
    def __init__(self, velocity, position):
        Thread.__init__(self)
        """
        Initializes drone data, connects to server, and sends data object to server
        Velocity, position, and name can be accessed through drone_object.data.x where x = field to be accessed
        :param velocity: the initial velocity of the drone
        :param position: the initial position of the drone
        """
        drone_id = uuid.uuid4().hex             # generates a unique ID based off the program run
        self.data = DroneData(velocity, position, drone_id)   # initialize data
        self.socket = drone_connect()                     # send connect message to server and initializes drone socket
        print(self.socket.getsockname())
        drone_send_info(self.socket, self.data)           # send initial drone info to server
        self.neighbors = drone_receive_info(self.socket)  # receive initial neighbor list

    def droneRules(self):
        # stay in the box
        movement_influence_vector = []
        for i in range(3):
            if self.data.position[i] + 50 >= FIELDDIM:
                movement_influence_vector.append(-100 / (abs(FIELDDIM - self.data.position[i]) + 1))
            else:
                movement_influence_vector.append(0)

            if self.data.position[i] - 50 <= 0:
                movement_influence_vector.append(100 / (abs(self.data.position[i]) + 1))
            else:
                movement_influence_vector.append(0)

        self.data.velocity = add_vectors(self.data.velocity, movement_influence_vector)
        self.data.position = add_vectors(self.data.position, self.data.velocity)

    def run(self):
        """
        The logic that adjusts each drone's positioning based off of the drones within its field of vision
        :return:
        """
        drone_send_info(self.socket, self.data)
        while 1:
            sleep(.1)
            self.neighbors = drone_receive_info(self.socket)
            self.droneRules()
            drone_send_info(self.socket, self.data)


def add_vectors(v1, v2):
    """
    Adds 2 vectors tuples together
    :param v1: the first vector
    :param v2: the second vector
    :return: a new sum vector
    """
    newTuple = (v1[0] + v2[0],
                v1[1] + v2[1],
                v1[2] + v2[2])
    return newTuple


def init_drone_field(threads):
    for i in range(3, 4):
        newDrone = Drone((-10.0, 0.0, -5.0), (100, 100, 100))
        threads.append(newDrone)
    for drone in threads:
        drone.start()
        sleep(.1)

    while 1:
        pass


def main():
    drone_threads = []
    # TEST DRONE COMMUNICATION ETC HERE
    init_drone_field(drone_threads)


if __name__ == '__main__':
    main()