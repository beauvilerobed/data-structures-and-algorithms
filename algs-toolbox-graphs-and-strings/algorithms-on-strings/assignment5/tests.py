from file_reader import read_multiple_files
import unittest
from suffix_tree import build_suffix_tree


files = read_multiple_files()

cases = list()
solutions = list()
for name in files:
    if name[-2:] == '.a':
        with open(name, 'r') as f:
            lines = f.readlines()
            lines = list(map(lambda x: x.strip(), lines))
            solutions.append(lines)
    else:
        with open(name, 'r') as f:
            line = f.readline().strip()
            cases.append(line)


class BuildSuffixTree(unittest.TestCase):
    def test(self):
        for case, solution in zip(cases, solutions):
            result = build_suffix_tree(case)
            result.sort()
            solution.sort()
            self.assertEqual(result, solution)


if __name__ == '__main__':
    unittest.main()
