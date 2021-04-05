from simulation import SIMULATION
import sys
s = sys.argv[1]
solutionID = sys.argv[2]
simulation = SIMULATION(s, solutionID)
simulation.Run()
simulation.Get_Fitness()

