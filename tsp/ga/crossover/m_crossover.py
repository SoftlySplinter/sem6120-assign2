from tsp.ga.crossover import CrossoverStrategy
from tsp.ga.chromosome import Chromosome

class MCrossoverOperator(CrossoverStrategy):
  def __init__(self):
    self.splits = 3

  def crossover(self, p1, p2):
    split1 = len(p1.genes) / self.splits
    split2 = len(p1.genes) - split1
    
    p1Splits = self.get_splits(p1.genes, split1, split2)
    p2Splits = self.get_splits(p2.genes, split1, split2)

    children = []
    for i in xrange(self.splits):
      children += self.do_crossover(p1Splits[i], p2Splits, p1.graph)
      children += self.do_crossover(p2Splits[i], p1Splits, p2.graph)
    assert len(children) == 2 * self.splits * self.splits
    return sorted(children, key=lambda c: c.fitness())[:2]

  def get_splits(self, p, split1, split2):
    return [p[:split1], p[split1:split2], p[split2:]]

  def do_crossover(self, addition, splits, graph):
      children = [self.make_gene(addition, splits[:i], splits[i:])
                  for i in xrange(len(splits))]
      return [Chromosome(child, graph) for child in children]

  def make_gene(self, addition, start, end):
      genes = []
      for sec in start:
        genes += [i for i in sec if i not in addition]
      genes += addition
      for sec in end:
        genes += [i for i in sec if i not in addition]
      return genes
