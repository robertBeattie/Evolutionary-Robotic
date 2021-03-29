import os
from hillclimber import HILL_CLIMBER as hc

for i in range(5):
    os.system("python generate.py")
    os.system("python simulate.py")
