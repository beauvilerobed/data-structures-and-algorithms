from file_reader import read_multiple_files, return_cases
import unittest
from suffix_array_long import build_suffix_array


class BuildSuffixArray(unittest.TestCase):
    def test(self):
        files = read_multiple_files()
        cases, solutions = return_cases(files)
        for text, solution in zip(cases, solutions):
            result = " ".join(map(str, build_suffix_array(text)))
            self.assertEqual(result, solution)


if __name__ == '__main__':
    unittest.main()
