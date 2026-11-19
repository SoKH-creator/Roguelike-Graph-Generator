from dataclasses import dataclass

@dataclass
class Node:
    id: int
    node_type: str = "normal"


class Graph:
    def __init__(self):
        self.nodes: dict[int, Node] = {}
        self.adjacency: dict[int, set[int]] = {}

    def add_node(self, node_id: int, node_type: str = "normal"):
        if node_id in self.nodes:
            raise ValueError(f"Node {node_id} already exists")

        self.nodes[node_id] = Node(node_id, node_type)
        self.adjacency[node_id] = set()

    def add_edge(self, a: int, b: int):
        if a == b:
            raise ValueError(f"Cannot connect a node to itself")
        if a not in self.nodes:
            raise ValueError(f"Node {a} does not exist")
        if b not in self.nodes:
            raise ValueError(f"Node {b} does not exist")
        self.adjacency[a].add(b)
        self.adjacency[b].add(a)

    def get_neighbors(self, node_id: int) -> set[int]:
        if node_id not in self.nodes:
            raise ValueError(f"Node {node_id} does not exist")
        return self.adjacency[node_id].copy()

    def degree(self, node_id: int) -> int:
        if node_id not in self.nodes:
            raise ValueError(f"Node {node_id} does not exist")
        return len(self.adjacency[node_id])
    