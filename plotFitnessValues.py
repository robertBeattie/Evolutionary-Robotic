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
quadCollapsed = np.zeros(c.numberOfGenerations)
hexCollapsed = np.zeros(c.numberOfGenerations)
for g in range(c.numberOfGenerations):
    quadCollapsed[g] = np.mean(quadValues[:, g])
    hexCollapsed[g] = np.mean(hexValues[:, g])
print(quadCollapsed)
print(hexCollapsed)
quad = plt.plot(quadCollapsed,linewidth=4, label='Quadaped Fitness Values', color = 'blue')
hex = plt.plot(hexCollapsed,linewidth=2, label='Hexapod Fitness Values', color = 'orange')
plt.ylabel('Fitness')
plt.xlabel('Generation')
plt.title('A/B test Body Building')
plt.legend()
plt.show()