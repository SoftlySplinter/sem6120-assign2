from multiprocessing import Pool

from tsp.ga.crossover import CrossoverFactory
from tsp.ga.chromosome import Chromosome

class GA:
  def __init__(self, population, graph, selector, crossover, mutator):
    self.selector = selector
    self.crossover = crossover
    self.mutator = mutator 

    self.population = [Chromosome.random_init(graph) 
                       for _ in xrange(population)]

  def evaluate(self):
    return zip(map(self.evaluate_single, self.population), self.population)

  def evaluate_single(self, chromosome):
    return chromosome.fitness()

  def __str__(self):
    return ("Selection Scheme: {}\nCrossover Scheme: {}\nMutation Scheme: {}"
            .format(self.selector, self.crossover, self.mutator))

class GAFactory:
  @classmethod
  def getGA(cls, args, graph):
    population = 100
    selector = None
    crossover = CrossoverFactory().getStrategy(args.crossover)
    mutator = None

    return GA(population, graph, selector, crossover, mutator)
