from world import WORLD
from robot import ROBOT

import constants as c
import pybullet as p
import pybullet_data
import time


class SIMULATION:

    def __init__(self):
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())

        # add gravity
        p.setGravity(0, 0, c.DEFAULT_GRAVITY)

        self.world = WORLD()
        self.robot = ROBOT()
