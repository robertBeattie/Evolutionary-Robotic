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


    def Run(self):
        for i in range(c.LOOP_LENGTH):
            print(i)


            p.stepSimulation()
            #backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
            #frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
            '''
            pyrosim.Set_Motor_For_Joint(

                bodyIndex=robot,

                jointName="Torso_BackLeg",

                controlMode=p.POSITION_CONTROL,

                targetPosition=BackLeg_motorCommand[i],

                maxForce=c.LEG_MOTOR_MAX_FORCE)
            pyrosim.Set_Motor_For_Joint(

                bodyIndex=robot,

                jointName="Torso_FrontLeg",

                controlMode=p.POSITION_CONTROL,

                targetPosition=FrontLeg_motorCommand[i],

                maxForce=c.LEG_MOTOR_MAX_FORCE)
            '''
            time.sleep(c.SLEEP_RATE)