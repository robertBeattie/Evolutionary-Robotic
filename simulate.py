import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import numpy as np
import random
import constants as c
from simulation import SIMULATION

simulation = SIMULATION()
simulation.Run()

"""


backLegSensorValues = np.zeros(c.LOOP_LENGTH)
frontLegSensorValues = np.zeros(c.LOOP_LENGTH)

targetAngles = np.linspace(-c.PI, c.PI, c.LOOP_LENGTH)
FrontLeg_motorCommand = c.FRONT_LEG_AMPLITUDE * np.sin(c.FRONT_LEG_FREQUENCY * targetAngles + c.FRONT_LEG_PHASE_OFFSET)
BackLeg_motorCommand = c.BACK_LEG_AMPLITUDE * np.sin(c.BACK_LEG_FREQUENCY * targetAngles + c.BACK_LEG_PHASE_OFFSET)


p.disconnect()


#print(backLegSensorValues)
#np.save('data//backLegSensorValues.npy',backLegSensorValues)
#np.save('data//frontLegSensorValues.npy',frontLegSensorValues)
#np.save('data//targetAngles.npy',targetAngles)
#np.save('data//BackLeg_motorCommand.npy',BackLeg_motorCommand)
#np.save('data//FrontLeg_motorCommand.npy',FrontLeg_motorCommand)
exit()

"""