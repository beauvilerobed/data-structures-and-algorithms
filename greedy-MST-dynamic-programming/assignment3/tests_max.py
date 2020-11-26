import unittest
from max_weight_IS import max_weight_IS
from file_reader import generate_files, generate_inputs_outputs_max

max_weight_test_cases = '/tests2/*'
input_files, output_files, assignment, file_path_length =\
                                      generate_files(max_weight_test_cases)
inputs_outputs = generate_inputs_outputs_max(input_files, output_files,
                                             assignment, file_path_length)


class TestMaxIS(unittest.TestCase):
    def test_cases(self):
        count = 1
        for case, length, data in inputs_outputs:
            self.assertEqual(max_weight_IS(case[1:], length), data)
            print("passed case:", count)
            count += 1


if __name__ == '__main__':
    unittest.main()
