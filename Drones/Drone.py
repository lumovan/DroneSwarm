"""
Python 3.7
Drone.py
Jacob Colley
Mark Takatsuka
"""
from Networking.Networking import *

# global variable for the maximum acceleration a drone can do
MAX_ACCEL = 50
MIN_DISTANCE = 5


class DroneData:
    def __init__(self, position, velocity, id):
        self.position = position
        self.velocity = velocity
        self.id = id



class Drone:
    def __init__(self):
        self.data = DroneData()
        self.data.position = (0.0, 0.0, 0.0)
        self.socket = drone_connect()

# move drone forward in the x direction
    def update(self, drone_list):
        self.data.velocity = (1.0, 0.0, 0.0)






"""
average = 0
        if len(drone_list) != 0:
            for i in range(0, len(drone_list)):
                avg = 0.0
                for j in range(len(getattr(drone_list[i], 'position'))):
                    avg += j
                average += avg / 3
"""