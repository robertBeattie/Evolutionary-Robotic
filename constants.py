import numpy as np

# simulation gravity
DEFAULT_GRAVITY = -9.8

# How long the simulation should run for
LOOP_LENGTH = 10000

#
PI = np.pi
# Leg Forces
FRONT_LEG_AMPLITUDE = PI/4.0
FRONT_LEG_FREQUENCY = 20
FRONT_LEG_PHASE_OFFSET = 0

BACK_LEG_AMPLITUDE = PI/4.0
BACK_LEG_FREQUENCY = 20
BACK_LEG_PHASE_OFFSET = PI/2

# how hard the leg motor should apply force maximum
LEG_MOTOR_MAX_FORCE = 20
# time sleep rate
SLEEP_RATE = 1/480
