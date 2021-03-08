from sensor import SENSOR
from motor import MOTOR


class ROBOT:

    def __init__(self):
        s = 2
        m = 2

        self.sensor = SENSOR()
        self.motor = MOTOR()
