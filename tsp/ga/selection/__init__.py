__all__ = ['SelectionScheme', 'SelectionFactory']

class SelectionScheme(object):
  """
  Performs selection based on the best 10% of individuals in the population.
  """

  def select(self, population):
    import math
    return population[:int(math.ceil(len(population) * 0.1))]

  def __str__(self):
    return self.__doc__


class SelectionFactory:
  def __init__(self):
    self.schemes = {
      'default': SelectionScheme()
    }
  def get_scheme(self, scheme):
    if scheme in self.schemes:
      return self.schemes[scheme]
    raise Exception("{} is not a valid selection scheme".format(scheme))
