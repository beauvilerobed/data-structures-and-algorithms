import unittest
from mincut import do_iter_mincut
from file_reader import read_multiple_files

input_files, output_files, assignment, file_path_length = read_multiple_files()

inputs_outputs = []
for name1, name2 in zip(input_files, output_files):
  if name1[file_path_length + 5:] != name2[file_path_length + 6:]:
    print("input file", name1[file_path_length + 5:], "is not the same as output file", name2[file_path_length + 6:])
    break
  else:
    with open(name1, 'r') as f:
      graph = {}
      lines = f.readlines()
      for line in lines:
        values = list(map(int, line.split()))
        vertex = values[0]
        edges = values[1:]
        graph[vertex] = edges

    with open(name2, 'r') as f:
      line = f.readline()
      value = int(line)
    
    inputs_outputs.append([graph, value])

class TestMinCut(unittest.TestCase):
  def test_cases(self):
    count = 1
    for graph, output_data in inputs_outputs:
      self.assertEqual(do_iter_mincut(graph), output_data)
      print("passed:", count)
      count += 1


if __name__ == '__main__':
  unittest.main()