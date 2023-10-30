import networkx as nx

class DistrictGraph:
    def __init__(self):
        self.graph = nx.Graph()

    def add_edge(self, district1, district2, distance):
        self.graph.add_edge(district1, district2, weight=distance)

    def shortest_path(self, source, destination):
        try:
            path = nx.shortest_path(self.graph, source=source, target=destination, weight='weight')
            path_cost = nx.shortest_path_length(self.graph, source=source, target=destination, weight='weight')
            return path, path_cost
        except nx.NetworkXNoPath:
            return [], float("inf")

# Instantiate the graph and add edges
graph = DistrictGraph()
graph.add_edge("Mchinji", "Kasungu", 141)
graph.add_edge("Mchinji", "Lilongwe", 109)
graph.add_edge("Lilongwe", "Dedza", 92)
graph.add_edge("Lilongwe", "Dowa", 55)
graph.add_edge("Kasungu", "Dowa", 117)
graph.add_edge("Kasungu", "Ntchisi", 66)
graph.add_edge("Dowa", "Ntchisi", 38)
graph.add_edge("Dowa", "Salima", 67)
graph.add_edge("Ntchisi", "Nkhotakota", 66)
graph.add_edge("Nkhotakota", "Salima", 112)
graph.add_edge("Dedza", "Salima", 96)
graph.add_edge("Dedza", "Ntcheu", 74)

# Prompt the user for source and destination districts
source_district = input("Enter the source district (first letter must be in caps): ")
destination_district = input("Enter the destination district (first letter must be in caps): ")

path, path_cost = graph.shortest_path(source_district, destination_district)

if path:
    print(f"Shortest path from {source_district} to {destination_district}: {path}")
    print(f"Total distance: {path_cost}")
else:
    print(f"No path found from {source_district} to {destination_district}")
