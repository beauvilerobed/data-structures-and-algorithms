import unittest
from median_heap import median_heap
from file_reader import generate_files, generate_inputs_outputs


input_files, output_files, assignment, file_path_length = generate_files()
inputs_outputs = generate_inputs_outputs(input_files, output_files,
                                         assignment, file_path_length)


class TestMedianHeap(unittest.TestCase):
    def test_cases(self):
        count = 1
        for input_value, output_value in inputs_outputs:
            self.assertEqual(median_heap(input_value), output_value)
            print("passed test case:", count)
            count += 1


if __name__ == '__main__':
    unittest.main()
