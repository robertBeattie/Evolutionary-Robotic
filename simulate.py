import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import numpy as np
import math
import random

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

# add gravity
p.setGravity(0,0,-9.8)

# add environment and objects
planeId = p.loadURDF("plane.urdf")
robot = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate("body.urdf")
LOOP_LENGTH = 100000
backLegSensorValues = np.zeros(LOOP_LENGTH)
frontLegSensorValues = np.zeros(LOOP_LENGTH)

for i in range(LOOP_LENGTH):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

    pyrosim.Set_Motor_For_Joint(

        bodyIndex= robot,

        jointName="Torso_BackLeg",

        controlMode= p.POSITION_CONTROL,

        targetPosition= random.uniform(-math.pi/2.0, math.pi/2.0),

        maxForce= 20)
    pyrosim.Set_Motor_For_Joint(

        bodyIndex=robot,

        jointName="Torso_FrontLeg",

        controlMode=p.POSITION_CONTROL,

        targetPosition= random.uniform(-math.pi/2.0, math.pi/2.0),

        maxForce=20)

    time.sleep(1/240)
p.disconnect()
#print(backLegSensorValues)
np.save('data//backLegSensorValues.npy',backLegSensorValues)
np.save('data//frontLegSensorValues.npy',frontLegSensorValues)