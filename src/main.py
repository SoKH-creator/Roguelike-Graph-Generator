from core.graph import Graph

graph = Graph()

graph.add_node(0, "start")
graph.add_node(1)
graph.add_node(2, "end")

graph.add_edge(0, 1)
graph.add_edge(1, 2)

print("Neighbors:", graph.get_neighbors(1))
print("Degree:", graph.degree(1))

graph.add_node(3)

print("Neighbors:", graph.get_neighbors(3))
print("Degree:", graph.degree(3))