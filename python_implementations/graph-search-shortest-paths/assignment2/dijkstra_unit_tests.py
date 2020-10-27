import unittest
import os
from dijkstra import dijkstra, Node, Graph
from file_reader import read_multiple_files

input_files, output_files, assignment, file_path_length = read_multiple_files()
input_files.sort()
output_files.sort()
inputs_outputs = []
# TODO: file reading step has a doulble for loop
for name1, name2 in zip(input_files, output_files):
  if name1[file_path_length + 5:] != name2[file_path_length + 6:]:
    print("input file", name1[file_path_length + 5:], "is not the same as output file", name2[file_path_length + 6:])
    break
  else:
    graph = Graph()
    with open(name1, 'r') as f:
        lines = f.readlines()
        for data in lines:
            values = data.split()
            node = Node(int(values[0]))
            edges = values[1:]
            for edge in edges:
                edge_and_length = list(map(int, edge.split(',')))
                edge_node = Node(edge_and_length[0])
                node.vertices.append([edge_node, edge_and_length[1]])

            graph.vertices.append(node)

    with open(name2, 'r') as f:
        line = f.readline()
        output_data = list(map(int, line.split(',')))

    inputs_outputs.append([graph, output_data])


class TestDijkstra(unittest.TestCase):
    def test_case(self):
        count = 1
        for graph, output_data in inputs_outputs:
            self.assertEqual(dijkstra(graph), output_data)
            print("passed test case:", count)
            count += 1

if __name__ == '__main__':
    unittest.main()