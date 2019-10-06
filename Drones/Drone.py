"""
File name: Drone.py
Author: Jacob Colley ~ jac9748@rit.edu
        Mark Takatsuka ~ mrt9583@rit.edu
        Kyle Feguson ~ krf6081@rit.edu
Date created: 10/05/2019
Date last modified: 10/06/2019
Python Version: 3.7

JACOB COMMENT HERE
"""

from Networking.Networking import *

# global variable for the maximum acceleration a drone can do
MAX_ACCEL = 50
MIN_DISTANCE = 5


class DroneData:
    """
    DroneData packages the drone's velocity, position, and name together for ease of sending to the Space server
    """
    def __init__(self, velocity, position, name):
        self.velocity = velocity
        self.position = position
        self.name = name


class Drone:
    """
    Drone contains functionality for drone movement and keeps track of the following fields:
        - Data ~ an instance of DroneData that keeps track of velocity, position, and name of this drone
        - Socket ~ the connection this drone has to the Space server
        - Neighbors ~ a list of drones within the drone's view distance that the drone uses to position and move itself
    """
    def __init__(self, velocity, position, name):
        """
        Initializes drone data, connects to server, and sends data object to server
        Velocity, position, and name can be accessed through drone_object.data.x where x = field to be accessed
        :param velocity: the initial velocity of the drone
        :param position: the initial position of the drone
        :param name: the name of the drone
        """
        self.data = DroneData(velocity, position, name)  # initialize data
        self.socket = drone_connect()                    # send connect message to server and initializes drone socket
        drone_send_info(self.socket, self.data)          # send initial drone info to server
        # self.neighbors = KYLE IS IMPLEMENTING RECEPTION OF NEIGHBOR LIST FROM SERVER

# move drone forward in the x direction
    def update(self):
        """
        JACOB COMMENT HERE
        :return:
        """
        self.data.velocity = (1.0, 0.0, 0.0)


def main():
    # TEST DRONE COMMUNICATION ETC HERE
    print("Beaner")


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