import matplotlib.pyplot
import numpy as np
backLegSensorValues = np.load('data/backLegSensorValues.npy')
back = matplotlib.pyplot.plot(backLegSensorValues,linewidth=2, label='backLegSensorValues')
matplotlib.pyplot.legend()


frontLegSensorValues = np.load('data/frontLegSensorValues.npy')
front = matplotlib.pyplot.plot(frontLegSensorValues, color='red',linewidth=2, label='frontLegSensorValues')
matplotlib.pyplot.legend()
matplotlib.pyplot.show()

TargetAngles = np.load('data/targetAngles.npy')
front = matplotlib.pyplot.plot(TargetAngles, color='pink',linewidth=5, label='targetAngles')
matplotlib.pyplot.legend()
matplotlib.pyplot.show()

BackLeg_motorCommand = np.load('data/BackLeg_motorCommand.npy')
front = matplotlib.pyplot.plot(BackLeg_motorCommand, color='green',linewidth=5, label='Back Motor values')
matplotlib.pyplot.legend()

FrontLeg_motorCommand = np.load('data/FrontLeg_motorCommand.npy')
front = matplotlib.pyplot.plot(FrontLeg_motorCommand, color='yellow',linewidth=5, label='Front Motor values')
matplotlib.pyplot.legend()
matplotlib.pyplot.show()