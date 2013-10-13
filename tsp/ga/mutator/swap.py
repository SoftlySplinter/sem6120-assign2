import random

from tsp.ga.mutator import DefaultMutator

class SwapMutator(DefaultMutator):
  def mutate(self, chromosome):
    i = random.randint(0, len(chromosome.genes) - 1)
    j = random.randint(0, len(chromosome.genes) - 1)
    self.swap(chromosome, i, j)

  def swap(self, chromosome, i, j):
    temp = chromosome.genes[i]
    chromosome.genes[i] = chromosome.genes[j]
    chromosome.genes[j] = temp

class SwapAdjecentMutator(SwapMutator):
  def mutate(self, chromosome):
    i = random.randint(0, len(chromosome.genes) - 1)
    choice = [i-1, i+1]
    choice = filter(lambda x: x >= 0 and x < len(chromosome.genes), choice)
    j = random.choice(choice)
    self.swap(chromosome, i, j)
