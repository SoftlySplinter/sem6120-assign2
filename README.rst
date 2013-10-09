SEM/CSM6120 Assignment: October 2013
====================================

Solving Travelling Salesman Problems with Genetic Algorithms
------------------------------------------------------------

The Travelling Salesman Problem (TSP) can be defined as follows: Given a 
collection of cities and the cost of travelling between any two cities, find a 
route that visits each city once and returns to the starting point such that 
the overall distance travelled is minimised.

Several such example problems can be found here: 
http://www.iwr.uni-heidelberg.de/groups/comopt/software/TSPLIB95/index.html and
 http://www.tsp.gatech.edu/world/countries.html

The format of the data is as follows::

  NAME: dj38
  COMMENT: 38 locations in Djibouti
  COMMENT: Derived from National Imagery and Mapping Agency data
  COMMENT: This file is a corrected version of dj89, where duplications
  COMMENT:  have been removed.  Thanks to Jay Muthuswamy and others for
  COMMENT:  requesting data sets without duplications.
  TYPE: TSP
  DIMENSION: 38
  EDGE_WEIGHT_TYPE: EUC_2D
  NODE_COORD_SECTION
  1 11003.611100 42102.500000
  2 ...

The first line is the name of the problem, followed by zero or more lines of 
comments. The example above is taken from a data file of 38 locations in the 
country Djibouti.

The next line is the type of problem. You should only consider TSPs for this 
assignment. The dimension line shows the number of cities in the problem (in 
this case, 38). The line `EDGE_WEIGHT_TYPE` defines what the data contained in 
the file represents. In the example above, this is defined as `EUC_2D` which 
means that the data represents points in 2D space (for this assignment, only 
consider `EUC_2D` data).

This is then followed by `NODE_COORD_SECTION` and the data itself, in the 
following format::

  <City number><X co-ordinate><Y co-ordinate>


Your task for this assignment is to do the following:

1. Design and implement a genetic algorithm in a programming language of your 
   choice that can solve TSPs in the data format above.
2. Write a report describing the implemented system, justifying design 
   decisions and providing experimentation. You should limit yourself to 3000 
   words for the report.

The assignment is worth 60% of the marks for this course. The final report 
should be submitted on Blackboard in PDF format any time before 5pm on 
**Friday 1st November 2013**.

The assignment will be assessed in line with the assessment criteria for essays
given in the student handbook. You should work on your own for this assignment
and not share any material with other students (your attention is drawn to the 
plagiarism warning given in the Student Handbook).


Part 1: Implementing the system (10 marks)
##########################################

You should design and implement a GA for solving TSPs. For this, you will need 
to consider the representation (how to represent solutions), how to achieve 
crossover and mutation, and other issues (how to avoid looping, how to ensure 
valid solutions are produced). This should be carried out following good 
programming principles. For example, if you are using Java (or another OO 
language), show a sensible breakdown of classes and use of inheritance.

Provide suitable documentation and commenting for your program.

Your program should:

- Read in a data file and translate the co-ordinates to distances between 
  cities.
- Provide facilities for the user to set the usual GA parameters (crossover
  type, mutation rate, number of generations, population size).
- Output some statistics concerning the performance of the program on the TSP, 
  such as runtime, number of generations, best solution found etc.
 
You may find some resources on the web useful - feel free to look at these, but
you must avoid plagiarism.For example, using someone's pseudocode is fine if 
you reference it, but don't copy someone's actual code. You should be able to 
demonstrate that the code you have written is your own.

You should email the program (source code and compiled program) to 
rkj@aber.ac.uk any time before the deadline. You should include a sentence or 
two that describes how to run the program and set the various GA parameters.


Part 2: The report (50 marks)
#############################

For the first part of the report, show the design of the system, discussing the
choices you made in part 1.

Describe how you structured the program, what representation you chose, how you
 solved any problems encountered, etc. **[20marks]**

For the second part of the report, you should conduct experimentation using at 
least three small TSPs from the URLs above (or another source, if you prefer - 
please justify though) and analyse the results. Discuss aspects such as the 
time taken, number of generations to converge, the impact of different 
parameters: crossover operators, mutation probabilities, number of chromosomes,
etc. If your implementation is efficient enough, you may consider applying your
program to larger problems from the online datasets. **[30marks]**
