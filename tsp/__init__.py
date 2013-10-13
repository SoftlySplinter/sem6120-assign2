from tsp.graph import Graph

__all__ = ['Graph', 'main']

import time
import pygame
from argparse import ArgumentParser

from tsp.data import DataLoader
from tsp.ga import GAFactory

__all__ = ['min_node','max_node','main']

import tsp

min_node = (0, 0)
max_node = (0, 0)
diff_node = (0, 0)

def main():
  parser = ArgumentParser(description="Solving the TSP through GAs")
  parser.add_argument('data_file', metavar='D', nargs=1, 
                      help='The data file to load')
  parser.add_argument('-p', '--preprocess', dest='preprocess', default=True,
                      help='Preprocess the graph')
  parser.add_argument('--selection', dest='selection', default='default', 
                      help='Selection Scheme')
  parser.add_argument('--crossover', dest='crossover', default='default', 
                      help='Crossover Scheme')
  parser.add_argument('--mutator', dest='mutator', default='default', 
                      help='Mutation Scheme')
  args = parser.parse_args()
  d = DataLoader()
  
  g = d.load(args.data_file[0], preprocess=args.preprocess)

  tsp.max_node = (max(g.nodes.itervalues(), key=lambda x: x[0])[0],
                  max(g.nodes.itervalues(), key=lambda x: x[1])[1])
  tsp.min_node = (min(g.nodes.itervalues(), key=lambda x: x[0])[0],  
                  min(g.nodes.itervalues(), key=lambda x: x[1])[1])

  tsp.diff_node = (max_node[0] - min_node[0], max_node[1] - min_node[1])

  draw_map(g.nodes)
  ga = GAFactory.getGA(args, g)
  f = ga.population[0]
  while True:
    ga.step()
    f = ga.population[0]
    update_map(g.nodes, f.genes, f.score)
    
def draw_map(nodes):
  pygame.init()
  info = pygame.display.Info()
  screen = pygame.display.set_mode((info.current_w - 100,
                                    info.current_h - 100))
  screen.fill((255,255,255))
  map(draw_node, nodes.iteritems())
  pygame.display.flip()

def draw_node((id,node)):
  surface = pygame.display.get_surface()
  x = int((node[0] - tsp.min_node[0]) / tsp.diff_node[0] * surface.get_width())
  y = int((node[1] - tsp.min_node[1]) / tsp.diff_node[1] * surface.get_height())
  pygame.draw.circle(surface, (0, 0, 0), (x, y), 2)

def draw_path(path, nodes):
  surface = pygame.display.get_surface()
  path_forward = path[1:] + path[:1]
  for (i,j) in zip(path, path_forward):
    x1 = int((nodes[i][0] - tsp.min_node[0]) / tsp.diff_node[0] * surface.get_width())
    y1 = int((nodes[i][1] - tsp.min_node[1]) / tsp.diff_node[1] * surface.get_height())
    x2 = int((nodes[j][0] - tsp.min_node[0]) / tsp.diff_node[0] * surface.get_width())
    y2 = int((nodes[j][1] - tsp.min_node[1]) / tsp.diff_node[1] * surface.get_height())
    pygame.draw.line(surface, (100,100,100), (x1, y1), (x2, y2))


def update_map(nodes, best, score):
  import math
  screen = pygame.display.get_surface()
  screen.fill((255,255,255))
  map(draw_node, nodes.iteritems())
  draw_path(best, nodes)
  text = pygame.font.Font(pygame.font.get_default_font(), 12)
  t = text.render("Best distance: {}".format(score), True, (0,0,0))
  screen.blit(t, (0,0))
  pygame.display.flip()

if __name__ == "__main__":
  main()
