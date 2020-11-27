import unittest
from mincut import do_iter_mincut
from file_reader import generate_files, generate_cases


input_files, output_files, file_path_length = generate_files()
inputs_outputs = generate_cases(input_files, output_files, file_path_length)


class TestMinCut(unittest.TestCase):
    def test_cases(self):
        count = 1
        for graph, output_data in inputs_outputs:
            self.assertEqual(do_iter_mincut(graph), output_data)
            print("passed:", count)
            count += 1


if __name__ == '__main__':
    unittest.main()
