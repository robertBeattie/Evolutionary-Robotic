from solution import SOLUTION
import constants as c
import copy
import os

class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        os.system('del brain*.nndf')
        os.system('del fitness*.nndf')
        self.nextAvailableID = 0
        self.parents = {}
        #self.children = {}
        for i in range(c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1

    def Evolve(self):
        # self.parent.Evaluate("GUI")
        self.Evaluate(self.parents)
        exit()
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()


    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        #self.child.Evaluate("DIRECT")
        #self.Print()
        #self.Select()


    def Spawn(self):
        self.children = {}
        for s in range(len(self.parents)):
            self.parents[s].Set_ID()
            self.children[s] = copy.deepcopy(self.parents[s])
            self.nextAvailableID += 1

    def Mutate(self):
        for child in range(len(self.children)):
            child.Mutate()

    def Select(self):
        if self.parent.fitness > self.child.fitness:
            self.parent = self.child

    def Print(self):
        print('Parent:', self.parent.fitness, '<', 'Child:', self.child.fitness)

    def Show_Best(self):
        # self.parent.Evaluate("GUI")
        pass

    def Evaluate(self, solutions):
        for s in range(len(solutions)):
            solutions[s].Start_Simulation("GUI")
        for s in range(len(solutions)):
            solutions[s].Wait_For_Simulation_To_End()
