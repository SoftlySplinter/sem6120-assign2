from tsp.graph import Graph

__all__ = ['Graph', 'main']

from argparse import ArgumentParser

from tsp.data import DataLoader
from tsp.ga import GAFactory

def main():
  parser = ArgumentParser(description="Solving the TSP through GAs")
  parser.add_argument('data_file', metavar='D', nargs=1, 
                      help='The data file to load')
  parser.add_argument('-p', '--preprocess', dest='preprocess', default=True,
                      help='Preprocess the graph')
  parser.add_argument('--crossover', dest='crossover', default='default', 
                      help='Crossover Scheme')
  args = parser.parse_args()
  d = DataLoader()
  
  g = d.load(args.data_file[0], preprocess=args.preprocess)

  ga = GAFactory.getGA(args, g)
  print ga

if __name__ == "__main__":
  main()
