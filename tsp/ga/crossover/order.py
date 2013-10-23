import random
from tsp.ga.crossover import CrossoverStrategy

class Order1Crossover(CrossoverStrategy):
  """
    Order 1 Crossover:
    - Select a random swath of consecutive alleles from p1
    - Add these, in place, to c1
    - Remove these alleles from p2
    - Add these in order to the empty genes of c1
    - Swap p1 and p2 for c2.
  """ 

  def do_crossover(self, p1, p2):
    swath_s = random.randint(0, len(p1) - 1)
    swath_f = random.randint(swath_s, len(p1))
    swath = p1[swath_s:swath_f]
    temp = [gene for gene in p2 if gene not in swath]
    c1 = []
    for allele in p1:
      if allele in swath:
        c1.append(allele)
      else:
        c1.append(temp.pop())
    assert len(temp) == 0
    return c1
