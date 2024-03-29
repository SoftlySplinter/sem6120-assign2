import random

from tsp import graph

class Chromosome:
  @classmethod
  def random_init(cls, graph):
    """Create a Chromosome with a random set of genes."""
    alleles = [i for i in xrange(1, graph.dimension + 1)]
    random.shuffle(alleles)
    return Chromosome(alleles, graph)

  def __init__(self, genes, graph):
    self.genes = genes
    self.graph = graph
    self.score = None
    assert self.is_valid()

  def is_valid(self):
    return False not in map(lambda x: x in self.genes, 
                            xrange(1, len(self.genes)))

  def fitness(self):
    """Evaluate the fitness of a Chromosome."""
    if not self.score:
      self.score = sum([self.graph.distance(i,j) 
                       for (i,j) in zip(self.genes, 
                                        self.genes[1:] + self.genes[:1])])
    return self.score

  def __str__(self):
    return "{}".format(self.genes)

  def __repr__(self):
    return str(self.genes)
