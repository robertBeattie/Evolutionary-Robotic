from simulation import SIMULATION
import sys
s = sys.argv[1]
simulation = SIMULATION(s)
simulation.Run()
simulation.Get_Fitness()

