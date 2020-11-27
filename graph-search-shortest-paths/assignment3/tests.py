import unittest
from median_heap import median_heap
from file_reader import generate_files, generate_cases


input_files, output_files = generate_files()
inputs_outputs = generate_cases(input_files, output_files)


class TestMedianHeap(unittest.TestCase):
    def test_cases(self):
        for input_value, output_value in inputs_outputs:
            self.assertEqual(median_heap(input_value), output_value)


if __name__ == '__main__':
    unittest.main()
