import os
from scc import Node, Graph, find_scc
import unittest
from file_reader import read_multiple_files

input_files, output_files, assignment, file_path_length = read_multiple_files()

inputs_outputs = []
# TODO: prepocessing the has a doulble for loop
for name1, name2 in zip(input_files, output_files):
  if name1[file_path_length + 5:] != name2[file_path_length + 6:]:
    print("input file", name1[file_path_length + 5:], "is not the same as output file", name2[file_path_length + 6:])
    break
  else:
    graph = Graph()
    with open(name1, 'r') as f:
        for line in f.readlines():
            (_id, connecting_vertex) = (int(i) for i in line.split(' ', 1))
            if _id not in graph.nodes:
                graph.nodes[_id] = Node(_id, edges=[connecting_vertex])
            else:
                graph.nodes[_id].edges.append(connecting_vertex)
            
            if connecting_vertex not in graph.nodes:
                graph.nodes[connecting_vertex] = Node(connecting_vertex, edges=[-_id])
            else:
                graph.nodes[connecting_vertex].edges.append(-_id)

    with open(name2, 'r') as f:
        line = f.readline()
        data = list(map(int, line.split(',')))

    inputs_outputs.append([graph, data])
    print("finished processing file number", len(inputs_outputs))

class TestSCC(unittest.TestCase):
    def test_cases(self):
        count = 1
        for graph, data in inputs_outputs:
            self.assertEqual(find_scc(graph), data)
            print("passed test case:", count)
            count += 1

if __name__ == '__main__':
    unittest.main()
