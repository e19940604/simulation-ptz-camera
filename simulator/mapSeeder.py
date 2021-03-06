from thing import Thing
from camera import Camera
import numpy as np

class MapSeeder:
    SG_CAMERA_TIME = 10
    SG_CAMERA_RMAX = 5
    SG_CAMERA_VANGEL = np.pi / 3
    SG_CAMERA_RATIO = 1/3


    def __init__(self):
        """self.seedData = {
            'C' : [
                [1,3,4,6],
                [0,1,2,3,4,5,7],
                [0,2,4,5,7,8,9]
            ],
            'T': [
                [1,1,2],
                [3,0,1],
                [5,1,2],
                [3,0,1],
                [2,0,1,2],
                [5,1,2],
                [5,0],
                [3,1,2],
                [1,2],
                [2,2]
            ]
        }"""

        """self.seedData = {
            'C' : [
                [0,1,2,4,8],
                [0,1,3,5,6,8],
                [0,2,5,7,8,9]
            ],
            'T': [
                [1,0,1,2],
                [1,0,1],
                [2,0,2],
                [2,1],
                [3,0],
                [9,2],
                [1,1],
                [4,2],
                [1,0,1,2],
                [6,2]
            ]
        }"""

        """self.seedData = {
            'C' : [
                [2,3,5,6,7,8,9],
                [0,1,2,3,4,5,7,8,9],
                [0,1,4,7]
            ],
            'T' : [
                [3,1,2],
                [2,1,2],
                [2,0,1],
                [1,0,1],
                [1,1,2],
                [4,0,1],
                [1,0],
                [3,0,1,2],
                [8,0,1],
                [5,0,1]
            ]

        }"""

        """self.seedData = {
            'C' : [
                [0,1,2,3,4,5,6,7,8,[7.5,7.5]],
                [0,2,6,9,[4.16,5.61]],
                [0,1,9,[8.22,2.93]]
            ],
            'T' : [
                [10,0,1,2,[4.71,6.06]],
                [3,0,2,[10.50,4.99]],
                [1,0,1,[3.57,8.51]],
                [2,0,[10.86,7.43]],
                [2,0,[7.94,12.17]],
                [1,0,[9.44,9.37]],
                [5,0,1,[2.96,5.91]],
                [4,0,[5.37,11.64]],
                [1,0,[11.92,9.78]],
                [1,1,2,[5.47,1.45]]
            ]
        }"""

        self.seedData = {
            'C' : [
                [0,3,5,9,12,13,14,16,18,19,[15,15]],
                [0,3,6,7,8,9,11,13,15,[18.57,17.34]],
                [0,1,4,6,7,8,11,12,13,15,[17.78,20.03]],
                [4,6,7,10,11,[21.66,22.89]],
                [2,3,9,13,14,17,19,[15.77,12.20]]
            ],
            'T' : [
                [1,0,1,2,[18.42,17.14]],
                [2,2,[14.71,22.10]],
                [5,4,[13.40,9.57]],
                [2,0,1,4,[19.24,13.76]],
                [5,2,3,[18.65,22.70]],
                [1,0,[11.17,14.21]],
                [2,1,2,3,[22.04,19.76]],
                [7,1,2,[18.05,20.80]],
                [1,1,2,[20.72,16.44]],
                [1,0,1,4,[16.50,15.01]],
                [6,3,[23.32,25.03]],
                [1,1,2,3,[20.24,20.34]],
                [1,0,2,[13.51,19.32]],
                [1,0,1,2,4,[17.37,16.81]],
                [1,0,4,[17.25,12.48]],
                [6,1,2,[14.98,20.16]],
                [1,0,[11.76,16.52]],
                [2,4,[17.12,8.80]],
                [2,0,[11.95,18.40]],
                [2,0,4,[11.48,12.14]]
            ]
        }

    def mapObject(self):
        cameras = []
        things = []

        for i in range(5):
            c = Camera(i, self.SG_CAMERA_TIME, self.SG_CAMERA_RMAX, self.SG_CAMERA_VANGEL, self.SG_CAMERA_RATIO)
            cameras.append( c )

        for i in range(20):
            t = Thing(i, self.seedData['T'][i][0], 0)
            things.append(t)
            
        for c in cameras:
        
            for ti in self.seedData['C'][c.getIndex()]:
                if type(ti) == type([]):
                    c.setPosition(ti[0],ti[1])
                else:
                    c.addDetectableThing(things[ti])

        for t in things:
            for ci in self.seedData['T'][t.getIndex()][1:]:
                if type(ci) == type([]):
                    t.setPosition(ci[0],ci[1])
                else:
                    t.addDetectedCamera(cameras[ci])

        return cameras, things
