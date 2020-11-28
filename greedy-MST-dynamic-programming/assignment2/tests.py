import unittest
from clustering import cluster, largest_clusters
from file_reader import generate_files, generate_cases_cluster,\
                        generate_cases_cluster_large


input_files, output_files = generate_files()
inputs_outputs = generate_cases_cluster(input_files, output_files)


largest_clusters_test_cases = '/tests2/*'
input_files2, output_files2 = generate_files(largest_clusters_test_cases)
inputs_outputs2 = generate_cases_cluster_large(input_files2, output_files2)


class TestCluster(unittest.TestCase):
    # takes ~ 60 sec for both cases
    
    def test_cases(self):
        for graph, num_of_nodes, data in inputs_outputs:
            self.assertEqual(cluster(graph, num_of_nodes, k_cluster=4), data)

    def test_2_cases(self):
        for case, data in inputs_outputs2:
            self.assertEqual(largest_clusters(case, len(case)), data)


if __name__ == '__main__':
    unittest.main()
