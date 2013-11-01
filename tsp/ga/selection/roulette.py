import random

from tsp.ga.selection import SelectionScheme

class RouletteWheelSelection:
  def select(self, population):
    sum_fitness = sum(population, key=lambda x: x.fitness())
    selected = []
    return selected
# TODO     
#    return [individual for individual in population 
#            if random.random() < individual.fitness() / sum_fitness)]
