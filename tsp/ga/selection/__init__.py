__all__ = ['SelectionScheme', 'SelectionFactory']

class SelectionScheme(object):
  """
  Performs no selection at all
  """

  def select(self, population):
    return population

  def __str__(self):
    return self.__class__.__name__

from tsp.ga.selection.tournament import TournamentSelection
from tsp.ga.selection.roulette import RouletteWheelSelection

class SelectionFactory:
  def __init__(self):
    self.schemes = {
      'default': SelectionScheme(),
      'roulette': RouletteWheelSelection(),
      'tournament': TournamentSelection(),
    }
  def get_scheme(self, scheme):
    if scheme in self.schemes:
      return self.schemes[scheme]
    raise Exception("{} is not a valid selection scheme".format(scheme))
