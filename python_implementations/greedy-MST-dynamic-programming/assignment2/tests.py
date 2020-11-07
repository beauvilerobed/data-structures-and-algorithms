import unittest
from clustering import cluster, largest_clusters
from file_reader import generate_files, generate_inputs_outputs_cluster, generate_inputs_outputs_large_cluster


# set up test cases for clustering problem
input_files, output_files, assignment, file_path_length = generate_files()
print("finished returning first set of files")
inputs_outputs = generate_inputs_outputs_cluster(input_files, output_files, assignment, file_path_length)
print("finished generating first input output files")

# set up test cases for larger clustering problem
largest_clusters_test_cases = '/tests2/*'
input_files2, output_files2, assignment2, file_path_length2 = generate_files(largest_clusters_test_cases)
print("finished returning second set of files")
inputs_outputs2 = generate_inputs_outputs_large_cluster(input_files2, output_files2, assignment2, file_path_length2)
print("finished generating second input output files")

class TestCluster(unittest.TestCase):
    def test_cases(self):
        count = 1
        for graph, num_of_nodes, data in inputs_outputs:
            self.assertEqual(cluster(graph, num_of_nodes, k_cluster=4), data)
            print("passed case:", count)
            count += 1
    
    def test_2_cases(self):
        count = 1
        for case, data in inputs_outputs2:
            self.assertEqual(largest_clusters(case, len(case)), data)
            print("passed case:", count)
            count += 1


if __name__ == '__main__':
    unittest.main()