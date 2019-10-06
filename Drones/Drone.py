"""
Python 3.7
Drone.py
Jacob Colley
Mark Takatsuka
"""

# global variable for the maximum acceleration a drone can do
MAX_ACCEL = 50
MIN_DISTANCE = 5


class DroneData:
    position = (0.0, 0.0, 0.0)
    velocity = (0.0, 0.0, 0.0)
    id = ""



class Drone:
    position = (0.0, 0.0, 0.0)
    velocity = (0.0, 0.0, 0.0)
    id = ""

    data = DroneData()

    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity

# look at other drones to move away from drones that are too close by adjusting velocity
    def update(self, drone_list):
        average = 0
        if len(drone_list) != 0:
            for i in range(0, len(drone_list)):
                avg = 0.0
                for j in range(len(getattr(drone_list[i], 'position'))):
                    avg += j
                average += avg / 3




