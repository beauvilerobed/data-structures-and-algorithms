import unittest
from prims import prims
from file_reader import generate_files, generate_cases_prim


prims_test_cases = '/tests2/*'
input_files, output_files = generate_files(prims_test_cases)
cases = generate_cases_prim(input_files, output_files)


class TestPrim(unittest.TestCase):
    # takes ~ 24 sec
    def test_cases(self):
        for graph, data in cases:
            self.assertEqual(prims(graph, len(graph)), data)


if __name__ == '__main__':
    unittest.main()
