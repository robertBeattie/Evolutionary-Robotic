import numpy as np
import pyrosim.pyrosim as pyrosim
import random
import os
import time
import constants as c

class SOLUTION:
    def __init__(self, myID):
        self.myID = myID
        self.weights = np.random.rand(c.numSensorNeurons,c.numMotorNeurons)
        self.weights = self.weights * 2 -1

    def Evaluate(self, directOrGUI):
        pass

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        length = 1
        width = 1
        height = 1
        x = -3
        y = 3
        z = 0.5
        pyrosim.Send_Cube(name="Box", pos=[x, y, z], size=[length, width, height])

        pyrosim.End()

    def Generate_Body(self):
        # Create Robot
        pyrosim.Start_URDF("body.urdf")
        length = 1
        width = 1
        height = 1
        x = 0
        y = 0
        z = 1
        # Add Torso
        pyrosim.Send_Cube(name="Torso", pos=[x, y, z], size=[length, width, height])
        # Create Legs
        pyrosim.Send_Cube(name="FrontLeg", pos=[0, .5, 0], size=[0.2, 1, 0.2])
        pyrosim.Send_Cube(name="LowerFrontLeg", pos=[0, 0, -.5], size=[.2, .2, 1])
        pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg",type="revolute", position="0 0.5 1", jointAxis = "1 0 0")
        pyrosim.Send_Joint(name="FrontLeg_LowerFrontLeg", parent="FrontLeg", child="LowerFrontLeg",type="revolute", position="0 1 0", jointAxis = "1 0 0")

        pyrosim.Send_Cube(name="BackLeg", pos=[0, -.5, 0], size=[0.2, 1, 0.2])
        pyrosim.Send_Cube(name="LeftLeg", pos=[-.5, 0, 0], size=[1, 0.2, 0.2])
        pyrosim.Send_Cube(name="RightLeg", pos=[0.5, 0, 0], size=[1, 0.2, 0.2])

        # Create Lower Legs
        pyrosim.Send_Cube(name="LowerRightLeg", pos=[0, 0, -.5], size=[.2, .2, 1]) 
        pyrosim.Send_Cube(name="LowerLeftLeg", pos=[0, 0, -.5], size=[.2, .2, 1])
        pyrosim.Send_Cube(name="LowerBackLeg", pos=[0, 0, -.5], size=[.2, .2, 1])
        
        # Create Joints Upper
        
        pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg",type="revolute", position="0 -0.5 1", jointAxis = "1 0 0")
        pyrosim.Send_Joint(name="Torso_LeftLeg", parent="Torso", child="LeftLeg",type="revolute", position="-0.5 0 1", jointAxis = "0 1 0")
        pyrosim.Send_Joint(name="Torso_RightLeg", parent="Torso", child="RightLeg",type="revolute", position="0.5 0 1", jointAxis = "0 1 0")
        # create Joints Lower
        
        pyrosim.Send_Joint(name="BackLeg_LowerBackLeg", parent="BackLeg", child="LowerBackLeg",type="revolute", position="0 -1 0", jointAxis = "1 0 0")
        pyrosim.Send_Joint(name="LeftLeg_LowerLeftLeg", parent="LeftLeg", child="LowerLeftLeg",type="revolute", position="-1 0 0", jointAxis = "0 1 0")
        pyrosim.Send_Joint(name="RightLeg_LowerRightLeg", parent="RightLeg", child="LowerRightLeg", type="revolute", position="1 0 0", jointAxis = "0 1 0")

        pyrosim.End()

    def Generate_Brain(self):
        # Create World
        pyrosim.Start_NeuralNetwork("brain"+str(self.myID)+".nndf")
        pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="FrontLeg")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="BackLeg")
        pyrosim.Send_Sensor_Neuron(name=3, linkName="LeftLeg")
        pyrosim.Send_Sensor_Neuron(name=4, linkName="RightLeg")
                
        pyrosim.Send_Sensor_Neuron(name=5, linkName="LowerFrontLeg")
        pyrosim.Send_Sensor_Neuron(name=6, linkName="LowerBackLeg")
        pyrosim.Send_Sensor_Neuron(name=7, linkName="LowerLeftLeg")
        pyrosim.Send_Sensor_Neuron(name=8, linkName="LowerRightLeg")
        
        pyrosim.Send_Motor_Neuron(name=9 , jointName="Torso_FrontLeg")
        pyrosim.Send_Motor_Neuron(name=10, jointName="Torso_BackLeg")   
        pyrosim.Send_Motor_Neuron(name=11, jointName="Torso_LeftLeg")
        pyrosim.Send_Motor_Neuron(name=12, jointName="Torso_RightLeg")
                
        pyrosim.Send_Motor_Neuron(name=13, jointName="FrontLeg_LowerFrontLeg")
        pyrosim.Send_Motor_Neuron(name=14, jointName="BackLeg_LowerBackLeg")   
        pyrosim.Send_Motor_Neuron(name=15, jointName="LeftLeg_LowerLeftLeg")
        pyrosim.Send_Motor_Neuron(name=16, jointName="RightLeg_LowerRightLeg")


        # loop over the names
        for currentRow in range(c.numSensorNeurons):
            # loop over the motors
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow,
                                     targetNeuronName=currentColumn + c.numSensorNeurons,
                                     weight=self.weights[currentRow][currentColumn])
        
        pyrosim.End()

    def Mutate(self):
        randomRow = random.randint(0, c.numSensorNeurons -1)
        randomColumn = random.randint(0, c.numMotorNeurons-1)
        self.weights[randomRow,randomColumn] = random.random() * 2 -1

    def Set_ID(self):
        self.myID

    def Start_Simulation(self, directOrGUI):
        self.Create_World()
        self.Generate_Body()
        self.Generate_Brain()
        os.system("start /B python simulate.py " + directOrGUI + " " + str(self.myID))


    def Wait_For_Simulation_To_End(self):
        while not os.path.exists("fitness" + str(self.myID) + ".txt"):
            time.sleep(0.01)
        fitnessFile = open("fitness" + str(self.myID) + ".txt", "r")
        self.fitness = float(fitnessFile.read())
        fitnessFile.close()
        os.system('del fitness' + str(self.myID) +'.txt')