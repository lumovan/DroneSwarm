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
    dronelist = []
    for i in range(1):
        dronelist.append(drone_connect())

    for i in range(10):
        data = DroneData()
        data.id = ""
        num = 0.0
        data.position = (num, num, num)
        data.velocity = (num, num, num)
        print(drone_send_info(dronelist[0], data))
        # sleep(1)
    dronelist[0].close

    # print(drone_send_info(s2, "drone 2 checking in"))
    # s2.close()
    # print(drone_send_info(s3, "drone 3 checking in"))
    # s3.close()


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