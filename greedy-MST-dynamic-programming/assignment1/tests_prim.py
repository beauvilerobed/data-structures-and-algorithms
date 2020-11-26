import unittest
from prims import prims
from file_reader import generate_files, generate_inputs_outputs_prim


prims_test_cases = '/tests2/*'
input_files, output_files, assignment, file_path_length =\
                           generate_files(prims_test_cases)
inputs_outputs = generate_inputs_outputs_prim(input_files, output_files,
                                              assignment, file_path_length)


class TestPrim(unittest.TestCase):
    def test_cases(self):
        count = 1
        for graph, data in inputs_outputs:
            self.assertEqual(prims(graph, len(graph)), data)
            print("passed case:", count)
            count += 1


if __name__ == '__main__':
    unittest.main()
