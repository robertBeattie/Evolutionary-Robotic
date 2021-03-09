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
targetAngles = np.linspace(-c.PI, c.PI, c.LOOP_LENGTH)

exit()
"""