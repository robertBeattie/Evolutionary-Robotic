class MOTOR:

    def __init__(self, jointName):
        self.jointName = jointName
        self.Prepare_To_Act()

    def Prepare_To_Act(self):
        FrontLeg_motorCommand = c.FRONT_LEG_AMPLITUDE * np.sin(
            c.FRONT_LEG_FREQUENCY * targetAngles + c.FRONT_LEG_PHASE_OFFSET)


