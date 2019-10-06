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
import random
import math
import numpy as np

# global variable for the maximum acceleration a drone can do
MAX_ACCEL = 1
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
        self.maxSpeed = 10
        self.maxSteer = 20


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
        # currPos = np.array([self.data.position[0], self.data.position[1], self.data.position[2]])
        # currVel = np.array([self.data.velocity[0], self.data.velocity[1], self.data.velocity[2]])

        # movement_influence_vector = []
        for i in range(3):
            if self.data.position[i] + 50 >= FIELDDIM:
                self.data.velocity[i] += min((-100 / (abs(FIELDDIM - self.data.position[i]) + 1)), -MAX_ACCEL)

            if self.data.position[i] - 50 <= 0:
                self.data.velocity[i] += max((100 / (abs(self.data.position[i]) + 1)), MAX_ACCEL)

        self.data.position = self.addVec(self.data.position, self.data.velocity)

    def addVec(self, v1, v2):
        v1[0] += v2[0]
        v1[1] += v2[1]
        v1[2] += v2[2]

        return v1

    def limitForce(self):
        pass

    def getMagnitude(self, vector):
        return math.sqrt(vector[0] * vector[0] + vector[1] * vector[1] + vector[2] * vector[2])

    def normalize(self, vector):
        mag = self.getMagnitude(vector)
        return [vector[0]/mag, vector[1]/mag, vector[2]/mag]


    def run(self):
        """
        The logic that adjusts each drone's positioning based off of the drones within its field of vision
        :return:
        """
        drone_send_info(self.socket, self.data)
        while 1:
            self.neighbors = drone_receive_info(self.socket)
            self.droneRules()
            sleep(.1)
            drone_send_info(self.socket, self.data)

def init_drone_field(threads):
    for i in range(1):
        newDrone = Drone([random.randint(-5, 5), random.randint(-5, 5), random.randint(-5, 5)],
                         [random.randint(100, 900), random.randint(100, 900), random.randint(100, 900)])
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