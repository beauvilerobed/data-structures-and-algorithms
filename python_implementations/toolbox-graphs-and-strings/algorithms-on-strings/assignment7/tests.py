from file_reader import read_multiple_files
import unittest
from suffix_array_long import build_suffix_array


files = read_multiple_files()

cases = list()
solutions = list()
for name in files:
    if name[-2:] == '.a':
        with open(name, 'r') as f:
            line = f.readline().strip()
            solutions.append(line)
    else:
        with open(name, 'r') as f:
            line = f.readline().strip()
            cases.append(line)


class BuildSuffixArray(unittest.TestCase):
    def test(self):
        for text, solution in zip(cases, solutions):
            result = " ".join(map(str, build_suffix_array(text)))
            self.assertEqual(result, solution)


if __name__ == '__main__':
    unittest.main()