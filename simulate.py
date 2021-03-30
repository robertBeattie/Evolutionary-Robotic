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
simulation.Get_Fitness()

