
__all__ = ['DefaultMutator', 'MutatorFactory']

class DefaultMutator(object):
  """
  Do not perform any form of mutation.
  """
  import random
  def mutate(self, chromosome):
    pass

  def __str__(self):
    return self.__class__.__name__

from tsp.ga.mutator.swap import SwapMutator, SwapAdjecentMutator
class MutatorFactory:
  def __init__(self):
    self.mutators = {
      'default': DefaultMutator(),
      'swap': SwapMutator(),
      'swap-adjecent': SwapAdjecentMutator(),
    }

  def get_mutator(self, mutator):
    if mutator in self.mutators:
      return self.mutators[mutator]
    raise Exception('No such mutator: {}'.format(mutator))
