from sensor import SENSOR
from motor import MOTOR
import pyrosim.pyrosim as pyrosim


class ROBOT:

    def __init__(self):
        pyrosim.Prepare_To_Simulate("body.urdf")
        Prepare_To_Sense()
        self.s = 2
        self.m = 2
        self.motor = MOTOR()

    def Prepare_To_Sense(self):
        self.sensor = SENSOR()
        for linkName in pyrosim.linkNamesToIndices:
            print(linkName)