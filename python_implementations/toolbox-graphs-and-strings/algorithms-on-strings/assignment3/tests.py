from file_reader import read_multiple_files
import unittest
from bwt import BWT


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


class BurrowsWheelerTransform(unittest.TestCase):
    def test(self):
        for case, solution in zip(cases, solutions):
            self.assertEqual(BWT(case), solution)


if __name__ == '__main__':
    unittest.main()