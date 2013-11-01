Installing
==========

Requirements
------------

* Python 2.7
* Pygame (http://www.pygame.org/)
* matplotlib (http://matplotlib.org/)
* numpy (http://www.numpy.org)
* setup tools (https://pypi.python.org/pypi/setuptools)
* progressbar (http://code.google.com/p/python-progressbar/)
* argparse (http://docs.python.org/dev/library/argparse.html)

Installation
------------

To install run::
  python ./setup.py install

The progressbar dependency can be installed through this method.

Can be run as root to be installed system-wide, or run as follows to be
installed as a user only::
  python ./setup.py --user install

A virtual environment can also be set up to keep this isolated from your
system. See http://www.virtualenv.org/en/latest/ for more information.

Running
-------

To run use::
  sem6120-tsp <args> FILE

All arguments do have defaults, but options like the mutator and crossover 
operator should be specified to get meaningful results.

Options
-------

Run the following command to see a list of all arguments and their usage::
  sem6120-tsp --help

Selection Schemes
-----------------

* `tournament` - Uses tournament selection.
* Empty or `default` - Does not perform selection.

Crossover Operators
-------------------

* `cycle` - Uses cycle crossover.
* `order1` - Users order crossover operator.
* `m-crossover` - Users m-crossover operator.

Mutation Operators
------------------

* `swap` - Uses swap operator.
* `swap-adjecent` - Uses swap adjacent operator.
