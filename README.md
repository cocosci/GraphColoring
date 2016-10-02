================================================================
	GRAPH COLORING & CSP/ BACKTRACKING & HEURESTIC APPROACH

											@author: Kai Zhen
											Student ID: zhenk
													  2015.11
================================================================

##How to run:

python radio.py legacy-constraints-#

================================================

##Where is the result:

After execution, there will be a txt file named results.txt

================================================

##What is the result like:

Two parts, the frequency assignment, and the number of backtracks.

Tennessee A


Rhode_Island B


North_Carolina B


......


Nevada D


Delaware A


Maine A


Number of backtracks:0


================================================

##Problem specification/Meethods:
It's a graph coloring problem, which is NP complete.
In order to resolve that, we need a backtrack algorithm.

Backtracking needs to be handled reasonably and wisely, 
otherwise it may cost huge time or may even not end.

We have four ways to optimize that.
1> Most constrained variable heuristic (or minimum remainder values MRV): chooses the variable with the fewest “legal” values 
2> Most constraining variable heuristic (or degree heuristic): among the variables with the smallest remaining domains (ties with respect to the most constrained variable heuristic), select the one that appears in the largest number of constraints on variables not in the current assignment
3> Least constraining value heuristic choses the variable that rules out the fewest values in the remaining variables 
4> Forward Checking: When X is assigned, look at each unassigned variable Y that is connected to X by a constraint and deletes from Y ’s domain any value that is inconsistent with the value chosen for X.

================================================
