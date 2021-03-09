from sensor import SENSOR
from motor import MOTOR
import pyrosim.pyrosim as pyrosim
import constants as c

class ROBOT:

    def __init__(self):
        pyrosim.Prepare_To_Simulate("body.urdf")
        self.sensors = {}
        self.Prepare_To_Sense()
        self.s = 2
        self.m = 2
        self.motor = {}
        self.values = {}



    def Prepare_To_Sense(self):

        for linkName in pyrosim.linkNamesToIndices:
           # print(linkName)
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self, t):

        for key in self.sensors:
            print(self.sensors)
            print(key)
            self.values[t] = self.sensors[key].Get_Value(t)
            if t == c.LOOP_LENGTH:
                print(self.sensors[key])

    def Prepare_To_Act(self):
        for jointName  in pyrosim.jointNamesToIndices:
            print(jointName)
            self.joints[jointName] = MOTOR(jointName)

