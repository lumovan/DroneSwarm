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
import random
from Networking.Networking import *
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

    def apply_velocity(self):
        """
        Adds velocity to position
        :return: None
        """
        newTuple = (self.position[0] + self.velocity[0],
                    self.position[1] + self.velocity[1],
                    self.position[2] + self.velocity[2])
        self.position = newTuple



class Drone:
    """
    Drone contains functionality for drone movement and keeps track of the following fields:
        - Data ~ an instance of DroneData that keeps track of velocity, position,
            and the name of this drone (a unique identifier generated upon drone creation)
        - Socket ~ the connection this drone has to the Space server
        - Neighbors ~ a list of drones within the drone's view distance that the drone uses to position and move itself
    """
    def __init__(self, velocity, position):
        """
        Initializes drone data, connects to server, and sends data object to server
        Velocity, position, and name can be accessed through drone_object.data.x where x = field to be accessed
        :param velocity: the initial velocity of the drone
        :param position: the initial position of the drone
        """
        drone_id = uuid.uuid4().hex             # generates a unique ID based off the program run
        self.data = DroneData(velocity, position, drone_id)   # initialize data
        self.socket = drone_connect()                     # send connect message to server and initializes drone socket
        drone_send_info(self.socket, self.data)           # send initial drone info to server
        self.neighbors = drone_receive_info(self.socket)  # receive initial neighbor list

    def update(self):
        """
        The logic that adjusts each drone's positioning based off of the drones within its field of vision
        :return:
        """
        self.data.apply_velocity()
        drone_send_info(self.socket, self.data)
        self.neighbors = drone_receive_info(self.socket)


def main():
    # TEST DRONE COMMUNICATION ETC HERE
    drone_list = []
    # make 10 drones with random x,y,z(0, FIELDDIM) and random velocity(-5, 5)
    for i in range(0, 10):
        drone_list.append(Drone(((round(random.uniform(0, FIELDDIM), 3)),
                              (round(random.uniform(0, FIELDDIM), 3)),
                              (round(random.uniform(0, FIELDDIM), 3))),
                             ((round(random.uniform(-5, 5), 3)),
                              (round(random.uniform(-5, 5), 3)),
                              (round(random.uniform(-5, 5), 3)))))
    # while True:
    #     for i in drone_list:
    #         if i.neighbors:
    #             for droneData in i.neighbors:
    #                 print(droneData.name, droneData.position, droneData.velocity)
    #         else:
    #             print("No neighbors :(")
    #         i.update()
    for i in drone_list:
        print(i)
            # sleep(.1)


if __name__ == '__main__':
    main()


"""
average = 0
        if len(drone_list) != 0:
            for i in range(0, len(drone_list)):
                avg = 0.0
                for j in range(len(getattr(drone_list[i], 'position'))):
                    avg += j
                average += avg / 3
"""