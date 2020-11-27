from file_reader import read_multiple_files, return_cases
import unittest
from bwt import BWT


class BurrowsWheelerTransform(unittest.TestCase):
    def test(self):
        files = read_multiple_files()
        cases, solutions = return_cases(files)
        for case, solution in zip(cases, solutions):
            self.assertEqual(BWT(case), solution)


if __name__ == '__main__':
    unittest.main()
