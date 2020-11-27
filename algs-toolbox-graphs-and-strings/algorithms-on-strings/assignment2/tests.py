from file_reader import read_multiple_files, return_cases
import unittest
from trie_matching import solve


class Solve(unittest.TestCase):
    def test(self):
        files = read_multiple_files()
        cases, solutions = return_cases(files)

        assert len(files) > 0
        assert len(cases) > 0
        assert len(solutions) > 0

        for case, solution in zip(cases, solutions):
            text = case[0]
            n = case[1]
            patterns = case[2:]
            self.assertEqual(solve(text, n, patterns), solution)


if __name__ == '__main__':
    unittest.main()
