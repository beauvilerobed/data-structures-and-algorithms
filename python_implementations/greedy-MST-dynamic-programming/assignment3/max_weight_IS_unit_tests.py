import unittest
from max_weight_IS import max_weight_IS
from file_reader import read_multiple_files

max_weight_test_cases = '/tests2/*'
input_files, output_files, assignment, file_path_length = read_multiple_files(max_weight_test_cases)

inputs_outputs = []
for name1, name2 in zip(input_files, output_files):
  if name1[file_path_length + 5:] != name2[file_path_length + 6:]:
    print("input file", name1[file_path_length + 5:], "is not the same as output file", name2[file_path_length + 6:])
    break
  else:
    case = []
    with open(name1, 'r') as f:
        lines = f.readlines()
        for line in lines:
            data = int(line)
            case.append(data)
        length = case[0]

    with open(name2, 'r') as f:
        line = f.readline()[:-1]
    
    inputs_outputs.append([case, length, line])

class TestMaxIS(unittest.TestCase):
    def test_cases(self):
        count = 1
        for case, length, data in inputs_outputs:
            self.assertEqual(max_weight_IS(case[1:], length), data)
            print("passed case:", count)
            count += 1


if __name__ == '__main__':
    unittest.main()
