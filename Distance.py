class LocationGraph:

  def __init__(self):
    self.nodes = {}

  def add_location(self, node, neighbors):
    self.nodes[node] = neighbors

  def get_distance(self, node1, node2):
    if node1 not in self.nodes or node2 not in self.nodes:
      return None  # Node not found in the graph

    if node2 in self.nodes[node1]:
      return self.nodes[node1][node2]

    return None  # Nodes are not adjacent


def main():
  # Example usage:
  graph = LocationGraph()

  # Add nodes and their distances to adjacent nodes
  graph.add_location("Cobeen", {"Schroeder": 5, "AMU": 7})
  graph.add_location("Schroeder", {"Cobeen": 5, "AMU": 2})
  graph.add_location("AMU", {"Cobeen": 7, "Schroeder": 2})
  graph.add_location("Straz", {"Cobeen": 5})

  # Calculate distance between nodes
  distance_1 = graph.get_distance("Schroeder", "AMU")
  distance_2 = graph.get_distance("Schroeder", "Cobeen")
  distance_3 = graph.get_distance("AMU", "Cobeen")
  distance_4 = graph.get_distance("Straz", "AMU")

  print(f"Minutes to walk between Schroeder and AMU: {distance_1}")
  print(f"Minutes to walk between Schroeder and Cobeen: {distance_2}")
  print(f"Minutes to walk between AMU and Cobeen: {distance_3}")
  print(f"Minutes to walk between AMU and Straz: {distance_4}")


main()
