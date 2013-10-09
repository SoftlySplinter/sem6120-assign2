
class CrossoverStrategy:
  def crossover(self, p1, p2):
    return p1

class CrossoverFactory:
  def __init__(self):
    self.strategies = {
                        "default": CrossoverStrategy()
                       }

  def getStrategy(self, strategy):
    if strategy not in self.strategies:
      raise Exception("{} not a valid stratergy".format(strategy))
    return self.strategies[strategy]
