from tsp.graph import Graph

__all__ = ['Graph', 'main']

import matplotlib.pyplot as plot
import numpy as np
import time

from argparse import ArgumentParser
from progressbar import ProgressBar

from tsp.data import DataLoader
from tsp.ga import GAFactory
from tsp.gui import GUI

def main():
  parser = ArgumentParser(description="Solving the TSP through GAs")
  parser.add_argument('data_file', metavar='D', nargs=1, 
                      help='The data file to load')
  parser.add_argument('-p', '--preprocess', dest='preprocess', default=False,
                      help='Preprocess the graph')
  parser.add_argument('--selection', dest='selector', default='default', 
                      help='Selection Scheme')
  parser.add_argument('--crossover', dest='crossover', default='default', 
                      help='Crossover Scheme')
  parser.add_argument('--mutator', dest='mutator', default='default', 
                      help='Mutation Scheme')
  parser.add_argument('--population', dest='population', default=100,
                      help='Population Size')
  parser.add_argument('--mutation-rate', dest='mutation_rate', default=0.01,
                      help='Mutation Rate')
  parser.add_argument('--crossover-rate', dest='crossover_rate', default=0.6,
                      help='Crossover Rate')
  parser.add_argument("--generations", dest="generations", 
                      help="Number of generations to run for.")
  parser.add_argument("--average", dest="average", help="Average over X runs")
  args = parser.parse_args()
  d = DataLoader()
  
  g = d.load(args.data_file[0], preprocess=args.preprocess)

  gui = GUI(g)
  run(int(args.generations), int(args.average), args, g, gui)

def run(total_generations, average_over, args, g, gui):
  print "Starting experiments. Averaging over {} runs.".format(average_over)
  best = []
  average = []

  progress = ProgressBar()
  gui.draw_map(True) 
  for i in progress(range(average_over)):
    (run_best, run_avg) = do_run(total_generations, args, g, gui)
    best.append(run_best)
    average.append(run_avg)

  print "Best result: {}".format(min([min(i) for i in best]))

  plot.plot(np.mean(best, axis=0), "b-", label="Best Fitness")
  plot.plot(np.mean(average, axis=0), "r-", label="Average Fitness")
  plot.legend()
  ga = GAFactory.getGA(args, g)
  plot.title("{}; {} nodes.".format(str(ga), g.dimension))
  plot.xlabel("Generations")
  # TODO make this a bit more solid.
  plot.ylim(ymin=9352, ymax=100000)
  plot.ylabel("Route Length (fitness)")
  plot.show()
  plot.savefig('report/img/results/{}n{}{}.png'.format(ga.file_path(), g.dimension, ga.file_name()), papertype='a4')

def do_run(total_generations, args, g, gui):
  ga = GAFactory.getGA(args, g)
  f = ga.population[0]
  average = []
  best = []
  for i in xrange(total_generations):
    ga.step()
    best.append(ga.population[0].score)
    average.append(np.mean([x.score for x in ga.population]))
    gui.update_map(ga.population)
  return (best, average)

if __name__ == "__main__":
  main()
