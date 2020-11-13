import unittest
from two_sums import find_two_sum_total
from file_reader import generate_files, generate_inputs_outputs


input_files, output_files, assignment, file_path_length = generate_files()
inputs_outputs = generate_inputs_outputs(input_files, output_files, assignment, file_path_length)

targets = [i for i in range(-10000, 10001)]


class TestTwoSums(unittest.TestCase):
    def test_cases(self):
        count = 1
        for input_value, output_value in inputs_outputs:
            self.assertEqual(find_two_sum_total(input_value, targets), output_value)
            print("passed test case:", count)
            count += 1


if __name__ == '__main__':
    unittest.main()