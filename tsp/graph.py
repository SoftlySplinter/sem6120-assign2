class Graph:
  def __init__(self):
    self.edge_weight_types = { "EUC_2D": self.euclidean_distance_2d }

    self.name = None
    self.comment = ""
    self.dimension = -1
    self.edge_weight_type = None
    self.nodes = {}

  def valid(self):
    print int(self.dimension) == len(self.nodes) and self.edge_weight_type in self.edge_weight_types
    return self.dimension == len(self.nodes) and self.edge_weight_type in self.edge_weight_types

  def distance(self, n1, n2):
    return self.edge_weight_types[self.edge_weight_type]

  def euclidean_distance_2d(self, n1, n2):
    return pow(n1.x - n2.x, 2) + pow(n1.y - n2.y, 2)

  def __str__(self):
    return 'Name: {}\nComments: \n{}Dimension: {}\nEdge Weight Type: {}'.format(self.name, self.comment, self.dimension, self.edge_weight_type)
