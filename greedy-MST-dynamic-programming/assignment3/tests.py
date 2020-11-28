import unittest
from huffman import compute_depth
from file_reader import generate_files, generate_inputs_outputs_huff,\
                                        generate_inputs_outputs_max
from max_weight_IS import max_weight_IS


input_files, output_files = generate_files()
inputs_outputs_huff = generate_inputs_outputs_huff(input_files, output_files)

max_weight_test_cases = '/tests2/*'
input_files, output_files = generate_files(max_weight_test_cases)
inputs_outputs_max = generate_inputs_outputs_max(input_files, output_files)


class TestHuffmanAndMax(unittest.TestCase):
    def test_cases_huff(self):
        for case, data in inputs_outputs_huff:
            self.assertEqual(compute_depth(case), data)

    def test_cases_max(self):
        for case, length, data in inputs_outputs_max:
            self.assertEqual(max_weight_IS(case[1:], length), data)


if __name__ == '__main__':
    unittest.main()
