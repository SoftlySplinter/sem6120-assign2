import random

from tsp.ga.selection import SelectionScheme

class TournamentSelection(SelectionScheme):
  """
  Runs tournaments between indivduals until a sufficient number are obtained.
  """

  def __init__(self):
    self.tournament_size = 5

  def select(self, population):
    selected = []
    while len(selected) < len(population):
      selected.append(self.run_tournament(random.sample(population,
                                                        self.tournament_size)))

    return selected

  def run_tournament(self, individuals):
    return sorted(individuals, key=lambda x: x.score)[0]
