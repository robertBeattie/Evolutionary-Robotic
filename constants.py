import numpy as np

# simulation gravity
DEFAULT_GRAVITY = -9.8

# How long the simulation should run for
LOOP_LENGTH = 5000

#
PI = np.pi
# Leg Forces
AMPLITUDE = PI/4.0
FREQUENCY = 20
PHASE_OFFSET = 0

targetAngles = np.linspace(-np.pi, np.pi, LOOP_LENGTH)
# how hard the leg motor should apply force maximum
LEG_MOTOR_MAX_FORCE = 20
# time sleep rate
SLEEP_RATE = 1/480 

numberOfGenerations = 1
## breaks on 100
populationSize = 1

motorJointRange = .4

numOfLegs = 6


numSensorNeurons = numOfLegs * 2
numMotorNeurons  = (numOfLegs * 2) +1