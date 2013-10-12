import random
from multiprocessing import Pool

from tsp.ga.crossover import CrossoverFactory
from tsp.ga.chromosome import Chromosome

class GA:
  def __init__(self, population, graph, selector, crossover, mutator, **kwargs):
    self.selector = selector
    self.crossover = crossover
    self.mutator = mutator

    self.crossover_rate = kwargs['crossover_rate'] if 'crossover_rate' in kwargs else 0.6
    self.mutation_rate = kwargs['mutation_rate'] if 'mutation_rate' in kwargs else 0.1

    self.population = [Chromosome.random_init(graph) 
                       for _ in xrange(population)]
    self.population = self.evaluate()

  def step(self):
    parents = self.population
    children = self.perform_crossover(parents)
    self.perform_mutation(children)
    self.population = self.perform_dismissal(parents, children)
    self.population = self.evaluate()
    

  def perform_crossover(self, parents):
    children = []
    while len(children) < len(self.population):
      if random.random() < self.crossover_rate:
        p1 = random.choice(parents)
        p2 = random.choice(parents)
        (c1, c2) = self.crossover.crossover(p1, p2)
        children += [c1, c2]
    return children

  def perform_mutation(self, children):
    to_mutate = [child for child in children 
                 if random.random < self.mutation_rate]
    self.mutator.mutate(to_mutate)

  def perform_dismissal(self, parents, children):
    temp = parents[:5] + children[5:]
    assert parents[0] == temp[0]
    return temp

  def evaluate(self):
    return sorted(map(self.evaluate_single, self.population), key=self.get_fitness)

  def get_fitness(self, chromosome):
    return chromosome.score

  def evaluate_single(self, chromosome):
    chromosome.score = chromosome.fitness()
    return chromosome

  def __str__(self):
    return ("Selection Scheme: {}\nCrossover Scheme: {}\nMutation Scheme: {}"
            .format(self.selector, self.crossover, self.mutator))

class GAFactory:
  @classmethod
  def getGA(cls, args, graph):
    population = 50
    selector = None
    crossover = CrossoverFactory().getStrategy(args.crossover)
    mutator = None

    return GA(population, graph, selector, crossover, mutator)
