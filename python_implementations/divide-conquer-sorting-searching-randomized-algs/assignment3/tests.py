import unittest
from count_sort import count_sort
from file_reader import read_multiple_files
import copy

input_files, output_files, assignment, file_path_length = read_multiple_files()

inputs_outputs1 = []
inputs_outputs2 = []
inputs_outputs3 = []
for name1, name2 in zip(input_files, output_files):
  if name1[file_path_length + 5:] != name2[file_path_length + 6:]:
    print("input file", name1[file_path_length + 5:], "is not the same as output file", name2[file_path_length + 6:])
    break
  else:
    with open(name1, 'r') as f:
      lines = f.readlines()
      input_data1 = list(map(int, lines))
      input_data2 = copy.copy(input_data1)
      input_data3 = copy.copy(input_data1)

    with open(name2, 'r') as f:
      lines = f.readlines()
      output_data1 = list(map(int, lines))
      output_data2 = copy.copy(output_data1)
      output_data3 = copy.copy(output_data1)

      inputs_outputs1.append([input_data1, output_data1])
      inputs_outputs2.append([input_data2, output_data2])
      inputs_outputs3.append([input_data3, output_data3])


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
