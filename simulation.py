from world import WORLD
from robot import ROBOT
import constants as c
import pybullet as p
import pybullet_data
import time


class SIMULATION:

    def __init__(self):
        p.connect(p.DIRECT)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())

        # add gravity
        p.setGravity(0, 0, c.DEFAULT_GRAVITY)

        self.world = WORLD()
        self.robot = ROBOT()

    def Run(self):
        for i in range(c.LOOP_LENGTH):
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act(i)

            time.sleep(c.SLEEP_RATE)

    def Get_Fitness(self):
        self.robot.Get_Fitness()

    def __del__(self):
        p.disconnect()
