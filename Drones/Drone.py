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
    position = (0.0, 0.0, 0.0)
    velocity = (0.0, 0.0, 0.0)
    name = ''


class Drone:
    def __init__(self, name, position, velocity):
        self.data = DroneData()
        self.data.velocity = velocity
        self.data.position = position
        self.data.name = name
        self.socket = drone_connect()

# move drone forward in the x direction
    def update(self, drone_list):
        self.data.velocity = (1.0, 0.0, 0.0)


def main():
    drone1 = Drone('One', (0.0, 0.0, 0.0), (0.0, 0.0, 0.0))
    print(drone_send_info(drone1.socket, drone1.data))


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