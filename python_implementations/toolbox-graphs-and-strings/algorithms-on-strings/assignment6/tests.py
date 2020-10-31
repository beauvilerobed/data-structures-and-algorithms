from file_reader import read_multiple_files
import unittest
from kmp import find_pattern


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
            lines = f.readlines()
            lines = list(map(lambda x: x.strip(), lines))
            cases.append(lines)


class FindPattern(unittest.TestCase):
    def test(self):
        for case, solution in zip(cases, solutions):
            pattern, text = case
            result = " ".join(map(str, find_pattern(pattern, text)))
            self.assertEqual(result, solution)


if __name__ == '__main__':
    unittest.main()