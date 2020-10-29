import unittest
from knapsack import knapsack, knapsack_fast
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
        data_set = f.readlines()
        values = []
        info = list(map(int, data_set[0].split()))
        number_items = info[1]
        knapsack_size = info[0]
        for value_pair in data_set[1:]:
            int_values = list(map(int, value_pair.split()))
            values.append(int_values)

    with open(name2, 'r') as f:
        line = f.readline()
        data = int(line)
    
    inputs_outputs.append([values, number_items, knapsack_size, data])


class TestKnapsack(unittest.TestCase):
    def test_cases(self):
        count = 1
        for case, num_items, knapsack_size, data in inputs_outputs:
            self.assertEqual(knapsack(case, num_items, knapsack_size), data)
            print("passed case:", count)
            count += 1

    def test_cases_fast(self):
        count = 1
        for case, num_items, knapsack_size, data in inputs_outputs:
            self.assertEqual(knapsack_fast(case, num_items, knapsack_size), data)
            print("passed case:", count)
            count += 1

if __name__ == '__main__':
    unittest.main()