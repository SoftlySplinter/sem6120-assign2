__all__ = ['CrossoverStrategy', 'CrossoverFactory']

from tsp.ga.chromosome import Chromosome

class CrossoverStrategy(object):
  """
  The default crossover scheme:
  - Crossover of parents (p1, p2) results in children (p1, p2).
  """

  def crossover(self, p1, p2):
    """Creates the two children by doing crossover of (p1, p2) and (p2, p1)."""
    return (Chromosome(self.do_crossover(p1.genes, p2.genes), p1.graph), 
            Chromosome(self.do_crossover(p2.genes, p1.genes), p2.graph))

  def do_crossover(self, p1, p2):
    """
    Performs crossover of parents (p1, p2). Resulting in children (p1, p2)
    """
    return [gene for gene in p1]

  def __str__(self):
    return self.__class__.__name__

class CrossoverFactory:
  def __init__(self):
    from tsp.ga.crossover.cycle import CycleCrossover
    from tsp.ga.crossover.order import Order1Crossover
    self.strategies = {
                        "default": CrossoverStrategy(),
                        "cycle":   CycleCrossover(),
                        "order1":  Order1Crossover(),
                       }

  def get_scheme(self, strategy):
    if strategy not in self.strategies:
      raise Exception("{} not a valid stratergy".format(strategy))
    return self.strategies[strategy]
