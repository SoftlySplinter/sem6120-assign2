import random

from tsp.ga.crossover import CrossoverStrategy

class CycleCrossover(CrossoverStrategy):
  """
  Performs crossover in a cyclic fashion:
  - The `i`th gene of p1 is replaced by that of the `i`th gene in p2.
  - `i` is then set to be the index of the replaced value in p2.
  - The above steps are repeated until `i` is the index it started at.
  """

  def crossover(self, p1, p2):
    (c1, c2) = super(CycleCrossover, self).crossover(p1, p2)
    assert c1 != p1
    assert c2 != p2
    return (c1, c2)

  def do_crossover(self, p1, p2):
    """
    Performs crossover in a cyclic fashion:
    - The `i`th gene of p1 is replaced by that of the `i`th gene in p2.
    - `i` is then set to be the index of the replaced value in p2.
    - The above steps are repeated until `i` is the index it started at.
    """
    # Duplicate the genes from p1
    offspring = [gene for gene in p1]

    i = random.randint(0, len(p1) - 1)
    start_i = i
    cycle = False

    # Perform the cycle crossover
    while not cycle:
      replaced = offspring[i]
      offspring[i] = p2[i]
      i = p2.index(replaced)
      cycle = i == start_i

    return offspring
