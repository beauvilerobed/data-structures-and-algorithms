import unittest
from count_inversion import sort_count
import os
import glob

file_path = os.getcwd() + '/tests/*'
file_path_length = len(file_path) - 1

paths = glob.glob(file_path)
input_files = []
output_files = []
assginment = ''
for path in paths:
  if path[file_path_length: file_path_length + 5] == 'input':
    input_files.append(path)
  elif path[file_path_length: file_path_length + 6] == 'output':
    output_files.append(path)
  else:
    assginment = path

input_files.sort()
output_files.sort()

inputs_outputs = []
for name1, name2 in zip(input_files, output_files):
  if name1[file_path_length + 5:] != name2[file_path_length + 6:]:
    print("input file", name1[file_path_length + 5:], "is not the same as output file", name2[file_path_length + 6:])
    break
  else:
    with open(name1, 'r') as f:
      lines = f.readlines()
      length = len(lines)
      input_data = list(map(int, lines))

    with open(name2, 'r') as f:
      line = f.readline()
      output_data = int(line)
      inputs_outputs.append([input_data, length, output_data])
  
class TestCountInversion(unittest.TestCase):
  def test_cases(self):
    count = 1
    for input_output in inputs_outputs:
      input_data = input_output[0]
      length = input_output[1]
      output_data = input_output[2]

      sort_count_final_result = sort_count(input_data, length)[1]
      self.assertEqual(sort_count_final_result, output_data)
      print('passed case', count)
      count += 1

if __name__ == '__main__':
  unittest.main()