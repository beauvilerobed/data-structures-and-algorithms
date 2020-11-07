import unittest
from count_sort import count_sort
from file_reader import generate_files, generate_input_outputs
import copy

input_files, output_files, assignment, file_path_length = generate_files()
inputs_outputs1, inputs_outputs2, inputs_outputs3 = \
            generate_input_outputs(input_files, output_files, assignment, file_path_length)


class TestCountSort(unittest.TestCase):
  def test_cases_right(self):
    count = 1
    for input_output in inputs_outputs1[1:]:    
      input_data = input_output[0]
      output_data = input_output[1]
      self.assertEqual(count_sort(input_data, 'right'), output_data[1])
      print('passed case', count)
      count += 1

  def test_cases_left(self):
    count = 1
    for input_output in inputs_outputs2[1:]:    
      input_data = input_output[0]
      output_data = input_output[1]
      self.assertEqual(count_sort(input_data, 'left'), output_data[0])
      print('passed case', count)
      count += 1

  def test_cases_middle(self):
    count = 1
    for input_output in inputs_outputs3[1:]:    
      input_data = input_output[0]
      output_data = input_output[1]
      self.assertEqual(count_sort(input_data, 'middle'), output_data[2])
      print('passed case', count)
      count += 1


if __name__ == '__main__':
  unittest.main()
