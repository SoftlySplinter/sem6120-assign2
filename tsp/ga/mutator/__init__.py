class DefaultMutator(object):
  def mutate(self, chromosome):
    """
    Do not perform any form of mutation.
    """
    pass

class MutatorFactory:
  def __init__(self):
    self.mutators = {
      'default': DefaultMutator()
    }

  def get_mutator(self, mutator):
    if mutator in self.mutators:
      return self.mutators[mutator]
    raise Exception('No such mutator: {}'.format(mutator))
