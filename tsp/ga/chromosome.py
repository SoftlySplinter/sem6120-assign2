import random

from tsp import graph

class Chromosome:
  @classmethod
  def random_init(cls, graph):
    """Create a Chromosome with a random set of genes."""
    alleles = [i for i in xrange(graph.dimension)]
    random.shuffle(alleles)
    return Chromosome(alleles, graph)

  def __init__(self, genes, graph):
    self.genes = genes
    self.graph = graph
    assert self.is_valid()

  def is_valid(self):
    for i in xrange(len(self.genes)):
      assert i in self.genes
    return True

  def fitness(self):
    """Evaluate the fitness of a Chromosome."""
    return sum([self.graph.distance(i,j) 
                for (i,j) in zip(self.genes, self.genes[:1] + self.genes[0])])

  def __str__(self):
    return "{}".format(self.genes)

  def __repr__(self):
    return str(self.genes)
