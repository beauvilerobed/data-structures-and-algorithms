import unittest
from prims import prims
from file_reader import read_multiple_files

prims_test_cases = '/tests2/*'
input_files, output_files, assignment, file_path_length = read_multiple_files(prims_test_cases)

inputs_outputs = []
temp = []
for name1, name2 in zip(input_files, output_files):
  if name1[file_path_length + 5:] != name2[file_path_length + 6:]:
    print("input file", name1[file_path_length + 5:], "is not the same as output file", name2[file_path_length + 6:])
    break
  else:
    case = []
    with open(name1, 'r') as f:
        lines = f.readlines()
        for line in lines:
            data = list(map(int, line.split()))
            case.append(data)
    with open(name2, 'r') as f:
        line = f.readline()
        data = int(line)

    temp.append([case, data])

for input_output in temp:
  case = input_output[0]
  data = input_output[1]
  length = case[0][0]
  graph = {}
  for value in case[1:]:
    vertex = value[0]
    edge = value[1]
    edge_value = value[2]
    if vertex in graph:
      graph[vertex].append([edge, edge_value])
    else:
      graph[vertex] = [[edge, edge_value]]

    if edge != vertex:
      if edge in graph:
        graph[edge].append([vertex, edge_value])
      else:
        graph[edge] = [[vertex, edge_value]]
  inputs_outputs.append([graph, data])


class TestPrim(unittest.TestCase):
    def test_cases(self):
        count = 1
        for graph, data in inputs_outputs:
            self.assertEqual(prims(graph, len(graph)), data)  
            print("passed case:", count)
            count += 1     


if __name__ == '__main__':
    unittest.main()