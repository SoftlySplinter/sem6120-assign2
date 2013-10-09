from tsp.crossover import CrossoverFactory

def main():
  print "TSP"
  fact = CrossoverFactory()
  print fact.getStrategy("default").crossover("1","2")

if __name__ == "__main__":
  main()
