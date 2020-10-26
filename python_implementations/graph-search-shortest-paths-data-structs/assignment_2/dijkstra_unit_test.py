import unittest
import os
from dijkstra import dijkstra, Node, Graph

path = os.getcwd() + "/case.txt"

with open(path, 'r') as f:
    data_set = f.readlines()
    graph = Graph()

    for data in data_set:
        values = data.split()
        node = Node(int(values[0]))
        edges = values[1:]
        for edge in edges:
            edge_and_length = list(map(int, edge.split(',')))
            edge_node = Node(edge_and_length[0])
            node.vertices.append([edge_node, edge_and_length[1]])

        graph.vertices.append(node)

    dijkstra(graph)


