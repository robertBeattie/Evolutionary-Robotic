import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import numpy as np
import random
import constants as c


pass

"""
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

# add gravity
p.setGravity(0, 0, c.DEFAULT_GRAVITY)

# add environment and objects
planeId = p.loadURDF("plane.urdf")
robot = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate("body.urdf")

backLegSensorValues = np.zeros(c.LOOP_LENGTH)
frontLegSensorValues = np.zeros(c.LOOP_LENGTH)

targetAngles = np.linspace(-c.PI, c.PI, c.LOOP_LENGTH)
FrontLeg_motorCommand = c.FRONT_LEG_AMPLITUDE * np.sin(c.FRONT_LEG_FREQUENCY * targetAngles + c.FRONT_LEG_PHASE_OFFSET)
BackLeg_motorCommand = c.BACK_LEG_AMPLITUDE * np.sin(c.BACK_LEG_FREQUENCY * targetAngles + c.BACK_LEG_PHASE_OFFSET)

for i in range(c.LOOP_LENGTH):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

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

    time.sleep(c.SLEEP_RATE)
p.disconnect()


#print(backLegSensorValues)
#np.save('data//backLegSensorValues.npy',backLegSensorValues)
#np.save('data//frontLegSensorValues.npy',frontLegSensorValues)
#np.save('data//targetAngles.npy',targetAngles)
#np.save('data//BackLeg_motorCommand.npy',BackLeg_motorCommand)
#np.save('data//FrontLeg_motorCommand.npy',FrontLeg_motorCommand)
exit()

"""