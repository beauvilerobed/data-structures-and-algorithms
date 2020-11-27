from file_reader import read_multiple_files, return_cases
import unittest
from suffix_tree import build_suffix_tree


class BuildSuffixTree(unittest.TestCase):
    def test(self):
        files = read_multiple_files()
        cases, solutions = return_cases(files)
        for case, solution in zip(cases, solutions):
            result = build_suffix_tree(case)
            result.sort()
            solution.sort()
            self.assertEqual(result, solution)


if __name__ == '__main__':
    unittest.main()
