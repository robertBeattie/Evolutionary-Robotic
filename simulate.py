import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import numpy as np
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
LOOP_LENGTH = 10000
backLegSensorValues = np.zeros(LOOP_LENGTH)
frontLegSensorValues = np.zeros(LOOP_LENGTH)

FrontLeg_amplitude = np.pi/4.0
FrontLeg_frequency = 20
FrontLeg_phaseOffset =0

BackLeg_amplitude = np.pi/4.0
BackLeg_frequency = 20
BackLeg_phaseOffset = np.pi/2

targetAngles = np.linspace(-np.pi, np.pi, LOOP_LENGTH)
FrontLeg_motorCommand = FrontLeg_amplitude * np.sin(FrontLeg_frequency * targetAngles + FrontLeg_phaseOffset)
BackLeg_motorCommand = BackLeg_amplitude * np.sin(BackLeg_frequency * targetAngles + BackLeg_phaseOffset)

for i in range(LOOP_LENGTH):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")



    pyrosim.Set_Motor_For_Joint(

        bodyIndex= robot,

        jointName="Torso_BackLeg",

        controlMode= p.POSITION_CONTROL,

        targetPosition= BackLeg_motorCommand[i],

        maxForce= 20)
    pyrosim.Set_Motor_For_Joint(

        bodyIndex=robot,

        jointName="Torso_FrontLeg",

        controlMode=p.POSITION_CONTROL,

        targetPosition= FrontLeg_motorCommand[i],

        maxForce=20)

    time.sleep(1/480)
p.disconnect()
#print(backLegSensorValues)
np.save('data//backLegSensorValues.npy',backLegSensorValues)
np.save('data//frontLegSensorValues.npy',frontLegSensorValues)
np.save('data//targetAngles.npy',targetAngles)
np.save('data//BackLeg_motorCommand.npy',BackLeg_motorCommand)
np.save('data//FrontLeg_motorCommand.npy',FrontLeg_motorCommand)
exit()