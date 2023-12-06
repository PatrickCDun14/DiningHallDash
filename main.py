from Graph import Graph

graph=Graph("AdjMatrixUpdated.xlsx")
print("Brute force implementation ")
graph.BruteForce()
print("Approximation")
graph.approximateShortestPath()