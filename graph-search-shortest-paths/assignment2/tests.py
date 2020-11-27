import unittest
import os
from dijkstra import dijkstra, Node, Graph
from file_reader import generate_files, generate_cases

input_files, output_files, len_file = generate_files()
cases = generate_cases(input_files, output_files)


class TestDijkstra(unittest.TestCase):
    def test_case(self):
        count = 1
        for graph, output_data in cases:
            self.assertEqual(dijkstra(graph), output_data)
            print("passed test case:", count)
            count += 1

if __name__ == '__main__':
    unittest.main()
