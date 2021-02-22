import matplotlib.pyplot
import numpy as np
backLegSensorValues = np.load('data/backLegSensorValues.npy')
back = matplotlib.pyplot.plot(backLegSensorValues,linewidth=2, label='backLegSensorValues')
matplotlib.pyplot.legend()


frontLegSensorValues = np.load('data/frontLegSensorValues.npy')
front = matplotlib.pyplot.plot(frontLegSensorValues, color='red',linewidth=2, label='frontLegSensorValues')
matplotlib.pyplot.legend()
matplotlib.pyplot.show()