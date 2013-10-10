from tsp.graph import Graph
from tsp.data import DataLoader

def main():
  d = DataLoader()
  print d.load("data")

if __name__ == "__main__":
  main()
