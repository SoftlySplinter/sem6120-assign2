import random

from tsp.ga.crossover import CrossoverFactory
from tsp.ga.chromosome import Chromosome
from tsp.ga.mutator import MutatorFactory
from tsp.ga.selection import SelectionFactory

class GA:
  def __init__(self, population, graph, selector, crossover, mutator, 
               crossover_rate, mutation_rate):
    self.selector = selector
    self.crossover = crossover
    self.mutator = mutator

    self.crossover_rate = crossover_rate
    self.mutation_rate = mutation_rate

    self.population = [Chromosome.random_init(graph) 
                       for _ in xrange(population)]
    self.population = self.evaluate()

  def step(self):
    parents = self.selector.select(self.population)
    children = self.perform_crossover(parents)
    self.perform_mutation(children)
    self.population = self.perform_dismissal(self.population, children)
    self.population = self.evaluate()
    

  def perform_crossover(self, parents):
    children = []
    while len(children) < int(len(self.population) * self.crossover_rate):
      if random.random() < self.crossover_rate:
        p1 = random.choice(parents)
        p2 = random.choice(parents)
        (c1, c2) = self.crossover.crossover(p1, p2)
        children += [c1, c2]
    return children[:int(len(self.population) * self.crossover_rate)]

  def perform_mutation(self, children):
    to_mutate = [child for child in children 
                 if random.random() < self.mutation_rate]
    map(self.mutator.mutate, to_mutate)

  def perform_dismissal(self, parents, children):
    a = int(len(self.population) * self.crossover_rate)
    temp = parents[:len(self.population) - a] + children
    assert len(temp) == len(self.population)
    return temp

  def evaluate(self):
    return sorted(self.population, 
                  key = lambda x: x.fitness())

  def file_path(self):
    return "{}/{}/".format(str(self.crossover).lower(),
                           str(self.mutator).lower())

  def file_name(self):
    return "p{}c{}m{}".format(len(self.population),
                              str(self.crossover_rate).replace(".", ""),
                              str(self.mutation_rate).replace(".", ""))

  def __str__(self):
    return ("GA with P={} C={} M={}\n{}, {} and {}"
            .format(len(self.population), 
                    self.crossover_rate,
                    self.mutation_rate, 
                    self.selector, 
                    self.crossover, 
                    self.mutator))

class GAFactory:
  @classmethod
  def getGA(cls, args, graph):
    population = int(args.population)
    crossover_rate = float(args.crossover_rate)
    mutation_rate = float(args.mutation_rate)
    selector = SelectionFactory().get_scheme(args.selector)
    crossover = CrossoverFactory().get_scheme(args.crossover)
    mutator = MutatorFactory().get_mutator(args.mutator)

    return GA(population, graph, selector, crossover, mutator, crossover_rate,
              mutation_rate)
