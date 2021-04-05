from solution import SOLUTION
import constants as c
import copy


class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        # self.parent = SOLUTION()
        # self.child = SOLUTION()
        pass

    def Evolve(self):
        # self.parent.Evaluate("GUI")
        # currentGeneration in range(c.numberOfGenerations):
        #    self.Evolve_For_One_Generation()
        # self.Show_Best()
        pass

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate("DIRECT")
        self.Print()
        self.Select()

    def Spawn(self):
        self.child = copy.deepcopy(self.parent)

    def Mutate(self):
        self.child.Mutate()

    def Select(self):
        if self.parent.fitness > self.child.fitness:
            self.parent = self.child

    def Print(self):
        print('Parent:', self.parent.fitness, '<', 'Child:', self.child.fitness)

    def Show_Best(self):
        self.parent.Evaluate("GUI")
