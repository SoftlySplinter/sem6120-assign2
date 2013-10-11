import re

from tsp import Graph

class ParseException(Exception):
  pass

class DataLoader:
  def __init__(self):
    self.tokens = {"NAME": self.parse_name, 
                   "COMMENT": self.parse_comment, 
                   "TYPE": self.parse_type, 
                   "DIMENSION": self.parse_dimension, 
                   "EDGE_WEIGHT_TYPE": self.parse_edge_weight_type,
                   "NODE_COORD_SECTION": self.parse_node_coord_section,}
  
  def load(self, file_name):
    self.errors = {}
    self.parsing_nodes = False
    self.graph = Graph()

    with open(file_name, 'r') as fp:
      for line in fp:
        self.parse(line)

    if self.graph.valid():
      return self.graph
    raise ParseException('Invalid Graph')

  def parse(self, line):
    if(self.parsing_nodes):
      self.parse_node(line)
    else:
      self.parse_line(line)

  def parse_line(self, line):
    token = self.get_token(line)
    if token == None:
      raise ParseException("No valid token found in line: '{}'".format(line))
    self.tokens[token](re.match('^{} *:?(.*)$'.format(token), line).group(1).strip())

  def get_token(self, line):
    split = line.split(':')
    token = split[0].strip()
    if token in self.tokens:
      return token

  def parse_name(self, name):
    self.graph.name = name

  def parse_comment(self, comment):
    self.graph.comment += comment + '\n'

  def parse_type(self, type):
    if type != "TSP":
      raise ParseException("{} is not a valid type".format(type))

  def parse_dimension(self, dimension):
    self.graph.dimension = int(dimension)

  def parse_edge_weight_type(self, type):
    self.graph.edge_weight_type = type

  def parse_node_coord_section(self, _):
    self.parsing_nodes = True

  def parse_node(self, line):
    args = line.strip().split(" ")
    self.graph.nodes[int(args[0])] = (float(args[1]), float(args[2]))
