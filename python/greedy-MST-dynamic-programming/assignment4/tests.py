import unittest
from knapsack import knapsack, knapsack_fast
from file_reader import generate_files, generate_inputs_outputs

input_files, output_files, assignment, file_path_length = generate_files()
inputs_outputs = generate_inputs_outputs(input_files, output_files, assignment, file_path_length)


class TestKnapsack(unittest.TestCase):
    def test_cases(self):
        count = 1
        for case, num_items, knapsack_size, data in inputs_outputs:
            self.assertEqual(knapsack(case, num_items, knapsack_size), data)
            print("passed case:", count)
            count += 1

    def test_cases_fast(self):
        count = 1
        for case, num_items, knapsack_size, data in inputs_outputs:
            self.assertEqual(knapsack_fast(case, num_items, knapsack_size), data)
            print("passed case:", count)
            count += 1

if __name__ == '__main__':
    unittest.main()