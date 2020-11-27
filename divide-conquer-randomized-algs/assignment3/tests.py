import unittest
from count_sort import count_sort
from file_reader import generate_files, generate_cases


input_files, output_files, len_files = generate_files()
inputs_outputs1, inputs_outputs2, inputs_outputs3 = \
            generate_cases(input_files, output_files, len_files)


assert len(inputs_outputs1) > 0
assert len(inputs_outputs2) > 0
assert len(inputs_outputs3) > 0


class TestCountSort(unittest.TestCase):
    def test_cases_right(self):
        for input_output in inputs_outputs1[1:]:
            input_data = input_output[0]
            output_data = input_output[1]
            self.assertEqual(count_sort(input_data, 'right'), output_data[1])

    def test_cases_left(self):
        for input_output in inputs_outputs2[1:]:
            input_data = input_output[0]
            output_data = input_output[1]
            self.assertEqual(count_sort(input_data, 'left'), output_data[0])

    def test_cases_middle(self):
        for input_output in inputs_outputs3[1:]:
            input_data = input_output[0]
            output_data = input_output[1]
            self.assertEqual(count_sort(input_data, 'middle'), output_data[2])


if __name__ == '__main__':
    unittest.main()
