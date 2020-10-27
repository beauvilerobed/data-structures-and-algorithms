import os
from scc import Node, Graph, find_scc
import unittest

path = os.getcwd() + "/case.txt"

graph = Graph()

with open(path, 'r') as f:
    for line in f.readlines():
        (_id, con_vertex) = (int(i) for i in line.split(' ', 1))
        if _id not in graph.nodes:
            graph.nodes[_id] = Node(_id, edges=[con_vertex])
        else:
            graph.nodes[_id].edges.append(con_vertex)
        
        if con_vertex not in graph.nodes:
            graph.nodes[con_vertex] = Node(con_vertex, edges=[-_id])
        else:
            graph.nodes[con_vertex].edges.append(-_id)

class TestSCC(unittest.TestCase):
    def test_assignment(self):
        expected = [434821, 968, 459, 313, 211]
        actual = find_scc(graph)
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
