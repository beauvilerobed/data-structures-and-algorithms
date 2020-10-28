import unittest
from two_sums import find_two_sum_total
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
        for line in lines:
            case.append(int(line))
    
    with open(name2, 'r') as f:
        line = f.readline()
        data = int(line)

    inputs_outputs.append([case, data])

targets = [i for i in range(-10000, 10001)]


class TestTwoSums(unittest.TestCase):
    def test_cases(self):
        count = 1
        for input_value, output_value in inputs_outputs:
            self.assertEqual(find_two_sum_total(input_value, targets), output_value)
            print("passed test case:", count)
            count += 1


if __name__ == '__main__':
    unittest.main()