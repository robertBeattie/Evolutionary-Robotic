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

        for i in range(c.numOfLegs):
            
            name = "Leg" + str(i)
            upperLegSize = [0.2, 1, 0.2]
            # calulate postion

            ###degress of spereation
            spacing = 360/c.numOfLegs
            postion = i * spacing

            ##Right Side
            if postion <= 45 or postion > 315:
                UpperlegPostion = [0.5, 0, 0]

                upperJointPosition = "0.5 0 1"
                upperJointAxis = "0 1 0"

                lowerJointPosition = "1 0 0"
                lowerJointAxis = "0 1 0"
             
            ##Front Side
            elif postion <= 135:
                UpperlegPostion = [0, 0.5, 0]

                upperJointPosition = "0 0.5 1"
                upperJointAxis = "0 1 0"

                lowerJointPosition = "0 1 0"
                lowerJointAxis = "1 0 0"
            
            ##Left Side
            elif postion <= 225:
                UpperlegPostion = [-0.5, 0, 0]

                upperJointPosition = "-0.5 0 1"
                upperJointAxis = "1 0 0"

                lowerJointPosition = "-1 0 0"
                lowerJointAxis = "0 1 0"
            
            ##Back Side
            else:
                UpperlegPostion = [0, -0.5, 0]

                upperJointPosition = "0 -0.5 1"
                upperJointAxis = "0 1 0"

                lowerJointPosition = "-1 0 0"
                lowerJointAxis = "0 1 0"
                

            #generate upper leg
            pyrosim.Send_Cube(name="Uppper" + name, pos=UpperlegPostion, size=upperLegSize)
            #generate lower leg
            pyrosim.Send_Cube(name="Lower"+ name, pos=[0, 0, -.5], size=[.2, .2, 1]) 
            #generate upper joint
            pyrosim.Send_Joint(name="Torso_Uppper" + name, parent="Torso", child=name,type="revolute", position=upperJointPosition, jointAxis = upperJointAxis)
            #generate lower joint
            pyrosim.Send_Joint(name= "Uppper" + name +"_Lower"+ name, parent=name, child="Lower" + name,type="revolute", position=lowerJointPosition, jointAxis = lowerJointAxis)
            
        pyrosim.End()
        

    def Generate_Brain(self):
        # Create World
        pyrosim.Start_NeuralNetwork("brain"+str(self.myID)+".nndf")
        pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
        #Generate Sensors
        for i in range(c.numOfLegs):
            name = "Leg" + str(i)
            pyrosim.Send_Sensor_Neuron(name=i+1, linkName="Uppper" + name)
            pyrosim.Send_Sensor_Neuron(name=i+c.numOfLegs+1, linkName="Lower" + name)    

        #Generate Motors
        for j in range(c.numOfLegs):
            name = "Leg" + str(j)
            pyrosim.Send_Motor_Neuron(name=j+c.numOfLegs * 2+1 , jointName="Torso_Uppper" + name)
            pyrosim.Send_Motor_Neuron(name=j+c.numOfLegs * 3+1 , jointName="Uppper" + name +"_Lower"+ name)

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