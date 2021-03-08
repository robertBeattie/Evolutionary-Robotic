from sensor import SENSOR
from motor import MOTOR
import pyrosim.pyrosim as pyrosim


class ROBOT:

    def __init__(self):
        pyrosim.Prepare_To_Simulate("body.urdf")

        self.s = 2
        m = 2

        self.sensor = SENSOR()
        self.motor = MOTOR()
