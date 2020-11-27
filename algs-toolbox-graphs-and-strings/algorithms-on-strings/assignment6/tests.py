from file_reader import read_multiple_files, return_cases
import unittest
from kmp import find_pattern


class FindPattern(unittest.TestCase):
    def test(self):
        files = read_multiple_files()
        cases, solutions = return_cases(files)
        for case, solution in zip(cases, solutions):
            pattern, text = case
            result = " ".join(map(str, find_pattern(pattern, text)))
            self.assertEqual(result, solution)


if __name__ == '__main__':
    unittest.main()
