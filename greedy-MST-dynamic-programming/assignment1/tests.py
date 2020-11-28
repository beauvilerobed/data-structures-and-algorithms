import unittest
from prims import prims
from jobs import scheduling, scheduling_ratio
from file_reader import generate_files, generate_cases_prim,\
                                        generate_cases_jobs


input_files2, output_files2 = generate_files()
cases2 = generate_cases_jobs(input_files2, output_files2)


prims_test_cases = '/tests2/*'
input_files, output_files = generate_files(prims_test_cases)
cases = generate_cases_prim(input_files, output_files)


class TestPrimAndJobs(unittest.TestCase):
    # takes ~ 24 sec
    def test_cases(self):
        for graph, data in cases:
            self.assertEqual(prims(graph, len(graph)), data)
    
    def test_jobs_difference(self):
        for input_value, output_value in cases2:
            result = scheduling(input_value)
            result_ratio = scheduling_ratio(input_value)
            self.assertEqual([result, result_ratio], output_value)


if __name__ == '__main__':
    unittest.main()
