import unittest
from clustering import cluster, largest_clusters
from file_reader import read_multiple_files


# setting up test cases for clustering problem
input_files, output_files, assignment, file_path_length = read_multiple_files()
temp = []
for name1, name2 in zip(input_files, output_files):
  if name1[file_path_length + 5:] != name2[file_path_length + 6:]:
    print("input file", name1[file_path_length + 5:], "is not the same as output file", name2[file_path_length + 6:])
    break
  else:
    case = []
    with open(name1, 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = list(map(int, line.split()))
            case.append(line)

    with open(name2, 'r') as f:
        line = f.readline()
        data = int(line)
    
    temp.append([case, data])

inputs_outputs = []
for input_output in temp:
    case = input_output[0]
    data = input_output[1]

    graph = {}
    num_of_nodes = case[0][0]
    for vertex, edge, edge_weight in case[1:]:
        if vertex in graph:
            graph[vertex].append([edge, edge_weight])
        else:
            graph[vertex] = [[edge, edge_weight]]

    inputs_outputs.append([graph, num_of_nodes, data])

# setting up test cases for larger clustering problem
largest_clusters_test_cases = '/tests2/*'
input_files2, output_files2, assignment2, file_path_length2 = read_multiple_files(largest_clusters_test_cases)


temp2 = []
inputs_outputs2 = []
for name1, name2 in zip(input_files2, output_files2):
  if name1[file_path_length + 5:] != name2[file_path_length + 6:]:
    print("input file", name1[file_path_length + 5:], "is not the same as output file", name2[file_path_length + 6:])
    break
  else:
    case = []
    with open(name1, 'r') as f:
        lines = f.readlines()
        for line in lines[1:]:
            line = line.replace(" ", "")
            case.append(line[:-1])
    with open(name2, 'r') as f:
        line = f.readline()
        data = int(line)

    inputs_outputs2.append([case, data])


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