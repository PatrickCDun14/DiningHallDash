
class DiningHallNeighbors:

  def __init__(self):
    self.dining_halls = {}

  def add_dining_hall(self, hall, neighbors):
    self.dining_halls[hall] = neighbors

  def get_neighboring_halls(self, hall):
    if hall not in self.dining_halls:
      return []
    else:
      return list(self.dining_halls[hall].keys())


def main():

  dining_hall_graph = DiningHallNeighbors()

  # Add dining halls and their distances to adjacent dining halls
  dining_hall_graph.add_dining_hall("Cobeen", {"Schroeder": 5, "Straz": 4})
  dining_hall_graph.add_dining_hall("Schroeder", {"Cobeen": 5, "AMU": 4})
  dining_hall_graph.add_dining_hall("AMU", {"Schroeder": 4, "Annex": 2})
  dining_hall_graph.add_dining_hall("Annex", {"AMU": 2})
  dining_hall_graph.add_dining_hall("Straz", {"Cobeen": 4})

  # Find neighboring dining halls
  Schroeder = dining_hall_graph.get_neighboring_halls("Schroeder")
  AMU = dining_hall_graph.get_neighboring_halls("AMU")
  Annex = dining_hall_graph.get_neighboring_halls("Annex")
  Cobeen = dining_hall_graph.get_neighboring_halls("Cobeen")
  Straz= dining_hall_graph.get_neighboring_halls("Straz")

  choice = input("Enter Dining hall to see Neighboring ones: ")
  neighboringHalls = dining_hall_graph.get_neighboring_halls(choice)
  if neighboringHalls:
    print(f"Neighboring Dining Halls to {choice}: {neighboringHalls}")
  else:
    print(f"{choice} not found")



main()


