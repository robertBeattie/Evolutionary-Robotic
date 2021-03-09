import constants as c
import numpy as np
import pyrosim.pyrosim as pyrosim

class SENSOR:

    def __init__(self, linkName):
        self.values = np.zeros(c.LOOP_LENGTH)

        self.linkName = linkName

    def Get_Value(self, t):
        self.values[t] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
        return self.values
