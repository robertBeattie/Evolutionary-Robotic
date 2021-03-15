from sensor import SENSOR
from motor import MOTOR
import pyrosim.pyrosim as pyrosim
import constants as c
import pybullet as p
from pyrosim.neuralNetwork import NEURAL_NETWORK



class ROBOT:

    def __init__(self):
        self.robot = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate("body.urdf")
        self.sensors = {}
        self.motors = {}
        self.values = {}
        self.Prepare_To_Sense()
        self.Prepare_To_Act()
        self.nn = NEURAL_NETWORK("brain.nndf")



    def Prepare_To_Sense(self):

        for linkName in pyrosim.linkNamesToIndices:
           # print(linkName)
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self, t):
        for key in self.sensors:
            #print(self.sensors)
            #print(key)
            self.values[t] = self.sensors[key].Get_Value(t)
           # if t == c.LOOP_LENGTH:
                # print(self.sensors[key])

    def Prepare_To_Act(self):
        for jointName in pyrosim.jointNamesToIndices:
            #print(jointName)
            self.motors[jointName] = MOTOR(jointName)

    def Act(self, t):
        for key in self.motors:
            #print(self.motors)
            #print(key)
            self.motors[key].Set_Value(self.robot, t)
            #if t == c.LOOP_LENGTH:
            #print(self.motors[key])

    def Save_Values(self):
        for key in self.motors:
            self.motors[key].Save_Values()
        for key in self.sensors:
            self.sensors[key].Save_Values()

    def Think(self):
        self.nn.Print()
