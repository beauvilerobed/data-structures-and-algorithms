import unittest
import os
from dijkstra import dijkstra, Node, Graph
from file_reader import generate_files, generate_inputs_outputs

input_files, output_files, assignment, file_path_length = generate_files()
inputs_outputs = generate_inputs_outputs(input_files, output_files,
                                         assignment, file_path_length)


class TestDijkstra(unittest.TestCase):
    def test_case(self):
        count = 1
        for graph, output_data in inputs_outputs:
            self.assertEqual(dijkstra(graph), output_data)
            print("passed test case:", count)
            count += 1

if __name__ == '__main__':
    unittest.main()
