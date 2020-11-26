import unittest
from huffman import compute_depth
from file_reader import generate_files, generate_inputs_outputs_huff


input_files, output_files, assignment, file_path_length = generate_files()
inputs_outputs = generate_inputs_outputs_huff(input_files, output_files,
                                              assignment, file_path_length)


class TestHuffman(unittest.TestCase):
    def test_cases(self):
        count = 1
        for case, data in inputs_outputs:
            self.assertEqual(compute_depth(case), data)
            print("passed case:", count)
            count += 1


if __name__ == '__main__':
    unittest.main()
