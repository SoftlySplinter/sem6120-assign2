class Graph:
  def __init__(self):
    self.edge_weight_types = { "EUC_2D": self.euclidean_distance_2d }

    self.name = None
    self.comment = ""
    self.dimension = -1
    self.edge_weight_type = None
    self.nodes = {}
    self.distances = {}

  def valid(self):
    return (self.dimension == len(self.nodes) and  
            self.edge_weight_type in self.edge_weight_types)

  def distance(self, n1, n2):
    if (n1, n2) in self.distances:
      return self.distances[(n1, n2)]
    return self.edge_weight_types[self.edge_weight_type](self.nodes[n1],
                                                         self.nodes[n2])

  def euclidean_distance_2d(self, (x1, y1), (x2, y2)):
    return pow(x1 - x2, 2) + pow(y2 - y2, 2)

  def preprocess(self):
    for i in self.nodes:
      for j in self.nodes:
        self.distances[(i,j)] = self.distance(i, j)

  def __str__(self):
    return ('Name: {}\nComments: \n{}Dimension: {}\nEdge Weight Type: {}\n{}'
            .format(self.name, 
                    self.comment, 
                    self.dimension, 
                    self.edge_weight_type, 
                    self.nodes,))
