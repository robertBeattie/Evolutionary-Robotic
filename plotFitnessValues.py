import matplotlib.pyplot as plt
import numpy as np
import constants as c
quadValues = np.load('results4.npy')
#quad = matplotlib.pyplot.plot(quadValues[0,:],linewidth=2, label='Quadaped Fitness Values')
#matplotlib.pyplot.legend()

hexValues = np.load('results6.npy')
#hex = matplotlib.pyplot.plot(hexValues[0,:],linewidth=2, label='Hexapod Fitness Values')
#matplotlib.pyplot.legend()
#matplotlib.pyplot.show()

for p in range(c.populationSize):
    quad = plt.plot(quadValues[p,:],linewidth=4, label='Quadaped Fitness Values', color = 'blue')
    hex = plt.plot(hexValues[p,:],linewidth=2, label='Hexapod Fitness Values', color = 'orange')
    plt.ylabel('Fitness')
    plt.xlabel('Generation')
    plt.title('A/B test Body Building')
    plt.legend()
plt.show()