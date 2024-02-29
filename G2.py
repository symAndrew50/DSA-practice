# G -> (V,E)
from collections import namedtuple

Graph = namedtuple("Graph",["nodes", "edges"])

nodes = ["A", "B", "C", "D"]
edges = [
    ("A", "B"),
    ("A", "B"),

    ("A", "C"),
    ("A", "C"),

    ("A", "D"),
    ("A", "D"),

    ("B", "D"),
    ("C", "D")
]

G = Graph(nodes, edges)


def adj_list(graph):
    adj = {node: [] for node in graph.nodes}

    for edge in graph.edges:
        node1 = edge[0]
        node2 = edge[1]

        adj[node1].append(node2)
        adj[node2].append(node1)
    
    return adj

