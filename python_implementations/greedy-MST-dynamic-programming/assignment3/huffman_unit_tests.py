import unittest
from huffman import compute_depth
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
        lines = lines[1:]
        for line in lines:
            case.append(int(line))

    with open(name2, 'r') as f:
        lines = f.readlines()
        data = list(map(int, lines))
    
    inputs_outputs.append([case, data])


class TestHuffman(unittest.TestCase):
    def test_cases(self):
        count = 1
        for case, data in inputs_outputs:
            self.assertEqual(compute_depth(case), data)
            print("passed case:", count)
            count += 1


if __name__ == '__main__':
    unittest.main()

