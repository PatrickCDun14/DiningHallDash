class LocationGraph:

  def __init__(self):
    self.nodes = {}

  def add_location(self, node, neighbors):
    self.nodes[node] = neighbors

  def get_distance(self, node1, node2, explored=None, distanceTraveled=0):
    if explored is None:
      explored = []
    distance = 99999  #practically infinity for our purposes
    if node1 not in self.nodes or node2 not in self.nodes:
      return distance  # Node not found in the graph
    elif node2 in self.nodes[node1]:
      return self.nodes[node1][node2]
    else:
      explored.append(node1)
      for each in self.nodes[node1]:
        if each not in explored:
          dist = self.get_distance(each, node2, explored,
                                   distanceTraveled + self.nodes[node1][each])
          if dist is not None and dist < distance:
            distance = dist + distanceTraveled
      return distance
    #if node2 in self.nodes[node1]:  #main part of the program
    #return self.nodes[node1][node2]

    #return None  # Nodes have no path


def main():
  # Example usage:
  graph = LocationGraph()

  # Add nodes and their distances to adjacent nodes
  graph.add_location("Cobeen", {"Schroeder": 5, "Straz": 4})
  graph.add_location("Schroeder", {"Cobeen": 5, "AMU": 4})
  graph.add_location("AMU", {"Schroeder": 4, "Annex": 2})
  graph.add_location("Annex", {"AMU": 2})
  graph.add_location("Straz", {"Cobeen": 4})

  # Calculate distance between nodes
  distance_1 = graph.get_distance("Schroeder", "AMU")
  distance_2 = graph.get_distance("Schroeder", "Cobeen")
  distance_3 = graph.get_distance("AMU", "Annex")
  distance_4 = graph.get_distance("Straz", "Annex")
  distance_5 = graph.get_distance("AMU", "Chicago")

  print(f"Minutes to walk between Schroeder and AMU: {distance_1}")
  print(f"Minutes to walk between Schroeder and Cobeen: {distance_2}")
  print(f"Minutes to walk between AMU and the Annex: {distance_3}")
  print(f"Minutes to walk between Straz and the Annex: {distance_4}")
  print(f"Minutes to walk between AMU and Chicago: {distance_5}")
  #print(graph.nodes["Cobeen"])


main()
