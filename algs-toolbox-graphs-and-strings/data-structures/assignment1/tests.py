import unittest
from check_brackets import find_mismatch
from file_reader import read_files, generate_test_cases

files = read_files()
solutions, cases = generate_test_cases(files)


class CheckBrackets(unittest.TestCase):
    def test(self):
        for i in range(len(cases)):
            self.assertEqual(solutions[i], find_mismatch(cases[i]))


if __name__ == '__main__':
    unittest.main()
