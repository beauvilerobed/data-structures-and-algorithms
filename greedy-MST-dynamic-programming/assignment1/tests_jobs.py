from jobs import scheduling, scheduling_ratio
import unittest
from file_reader import generate_files, generate_inputs_outputs_jobs


input_files, output_files, assignment, file_path_length = generate_files()
inputs_outputs = generate_inputs_outputs_jobs(input_files, output_files,
                                              assignment, file_path_length)


class TestJobs(unittest.TestCase):
    def test_jobs_difference(self):
        count = 1
        for input_value, output_value in inputs_outputs:
            result = scheduling(input_value)
            result_ratio = scheduling_ratio(input_value)
            self.assertEqual([result, result_ratio], output_value)
            print("passed case:", count)
            count += 1


if __name__ == '__main__':
    unittest.main()
