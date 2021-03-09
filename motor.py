import constants as c
import numpy as np
import pyrosim.pyrosim as pyrosim
import pybullet as p

class MOTOR:

    def __init__(self, jointName):
        self.jointName = jointName
        self.joints = {}
        self.Prepare_To_Act()

    def Prepare_To_Act(self):
        self.amplitude = c.AMPLITUDE
        self.frequency = c.FREQUENCY
        self.offset = c.PHASE_OFFSET

        self.motorValue = self.amplitude * np.sin(self.frequency * c.targetAngles + self.offset)


    def Set_Value(self,robot,t):
        pyrosim.Set_Motor_For_Joint(

            bodyIndex=robot,

            jointName=self.jointName,

            controlMode=p.POSITION_CONTROL,

            targetPosition=self.motorValue,

            maxForce=20
        )
