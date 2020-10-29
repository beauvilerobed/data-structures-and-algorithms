from jobs import scheduling, scheduling_ratio
import unittest
from file_reader import read_multiple_files


input_files, output_files, assignment, file_path_length = read_multiple_files()

inputs_outputs = []
for name1, name2 in zip(input_files, output_files):
  if name1[file_path_length + 5:] != name2[file_path_length + 6:]:
    print("input file", name1[file_path_length + 5:], "is not the same as output file", name2[file_path_length + 6:])
    break
  else:
    case = []
    with open(name1, 'r') as f:
        lines = f.readlines()
        for line in lines[1:]:
            weight, length = list(map(int, line.split()))
            case.append([weight, length])
    with open(name2, 'r') as f:
        lines = f.readlines()
        data = list(map(int, lines))

    inputs_outputs.append([case, data])

class TestJobs(unittest.TestCase):
    def test_jobs_difference(self):
        count = 1
        for input_value, output_value in inputs_outputs:
            result = scheduling(input_value)
            result_ratio = scheduling_ratio(input_value)
            self.assertEqual([result, result_ratio], output_value)
            print("passed case:", count)
            count += 1

if __name__ == '__main__':
    unittest.main()