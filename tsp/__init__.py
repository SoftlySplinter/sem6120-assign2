from argparse import ArgumentParser

from tsp.graph import Graph
from tsp.data import DataLoader

def main():
  parser = ArgumentParser(description="Solving the TSP through GAs")
  parser.add_argument('data_file', metavar='D', nargs=1)
  args = parser.parse_args()
  d = DataLoader()
  print args.data_file
  g = d.load(args.data_file[0])
  g.preprocess()
  print g

if __name__ == "__main__":
  main()
