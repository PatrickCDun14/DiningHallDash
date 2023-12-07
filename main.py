"""
Description: This script is used to demonstrate the functioniality of the Graph class 
Author: Greg Occhiogrosso
Python Version: 3.10.0
Dependencies: Graph, time
"""

from Graph import Graph
import time 
graph=Graph("AdjMatrixUpdated.xlsx")

start = time.time()
print("Brute force implementation")
graph.BruteForce()
end=time.time()
bTime=end-start
print("The brute force algorithm finished in " + str(bTime)+ " seconds")
print("Approximation")
start=time.time()
graph.approximateShortestPath()
end=time.time()
aTime=end-start
print("The approximation algorithm finished in " + str(aTime)+ " seconds")
#added a small constant for numerical stability
print("The approximation was over "+str(int(bTime/(aTime+.000000000000001)))+" times faster than the brute force algorithm")
