import unittest
from count_inversion import sort_count
from file_reader import generate_files, generate_test_parameters


input_files, output_files, assignment, file_path_length = generate_files()
test_parameters = generate_test_parameters(input_files, output_files,
                                           assignment, file_path_length)


class TestCountInversion(unittest.TestCase):
    def test_cases(self):
        count = 1
        for test_parameter in test_parameters:
            input_data = test_parameter[0]
            length = test_parameter[1]
            output_data = test_parameter[2]

            sort_count_final_result = sort_count(input_data, length)[1]
            self.assertEqual(sort_count_final_result, output_data)
            print('passed case', count)
            count += 1


if __name__ == '__main__':
    unittest.main()
