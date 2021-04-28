import numpy as np
import pyrosim.pyrosim as pyrosim
import random
import os
import time
import constants as c
import math 

class SOLUTION:
    def __init__(self, myID):
        self.myID = myID
        self.weights = np.random.rand(c.numSensorNeurons,c.numMotorNeurons)
        self.weights = self.weights * 2 -1

    def Evaluate(self, directOrGUI):
        pass

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Sphere(name="BowlingBall" , pos=[-3,+3,0.5] , size=[0.5])
        pyrosim.End()

    def Generate_Body(self):
       # Create Robot
        pyrosim.Start_URDF("body.urdf")
        # Add Torso
        #pyrosim.Send_Cube(name="Torso", pos=[x, y, z], size=[length, width, height])
        pyrosim.Send_Sphere(name="Torso" , pos=[0,0,1] , size=[0.5])
        for i in range(c.numOfLegs):
            
            name = "Leg" + str(i)
            
            # calulate postion

            ###degress of spereation
            spacing = 360.0/c.numOfLegs
            postion = i * spacing

            x = math.cos(math.radians(float(postion)))/2
            y = math.sin(math.radians(float(postion)))/2
            upperlegPostion = [x, y, 0]

            upperJointPosition = str(x) + " " + str(y) +" 1"
            
            upperJointAxis = str(abs(y*2)) + " " + str(abs(x*2)) +" 0"
            lowerJointPosition = str(x*2)+ " " + str(y*2)+" 0"
            lowerJointAxis = str(abs(y*2)) + " " + str(abs(x*2)) +" 0"

           
            #print('leg#:',i,"Postion:",postion)
            #print('leg',i,', upperJointPosition:',upperJointPosition)
            #print('leg',i,', upperJointAxis',upperJointAxis)
            #print('leg',i,', lowerJointPosition',lowerJointPosition)
            #print('leg',i,', lowerJointAxis',lowerJointAxis,'\n')

            #generate upper leg
            pyrosim.Send_Cube(name="Uppper" + name, pos=upperlegPostion,rpy=[0,0,math.radians(float(postion))], size=[1, 0.2, 0.2])
            #generate lower leg
            pyrosim.Send_Cube(name="Lower"+ name, pos=[0, 0, -.5],rpy=[0,0,math.radians(float(postion))], size=[.2, .2, 1]) 
            #generate upper joint
            pyrosim.Send_Joint(name="Torso_Uppper" + name, parent="Torso", child="Uppper" +name,type="revolute", position=upperJointPosition, jointAxis = upperJointAxis)
            #generate lower joint
            pyrosim.Send_Joint(name= "Uppper" + name +"_Lower"+ name, parent="Uppper" +name, child="Lower" + name,type="revolute", position=lowerJointPosition, jointAxis = lowerJointAxis)
            
        pyrosim.End()
        #exit()
    def Generate_Brain(self):
        nameCount = 0

        # Create World
        pyrosim.Start_NeuralNetwork("brain"+str(self.myID)+".nndf")
        pyrosim.Send_Sensor_Neuron(name=nameCount, linkName="Torso")
        nameCount += 1
        #Generate Sensors
        for i in range(c.numOfLegs):
            name = "Leg" + str(i)
            pyrosim.Send_Sensor_Neuron(name=nameCount, linkName="Uppper" + name)
            nameCount +=1
            pyrosim.Send_Sensor_Neuron(name=nameCount, linkName="Lower" + name)    
            nameCount +=1

        #Generate Motors
        for j in range(c.numOfLegs):
            name = "Leg" + str(j)
            pyrosim.Send_Motor_Neuron(name=nameCount , jointName="Torso_Uppper" + name)
            nameCount +=1
            pyrosim.Send_Motor_Neuron(name=nameCount , jointName="Uppper" + name +"_Lower"+ name)
            nameCount +=1

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