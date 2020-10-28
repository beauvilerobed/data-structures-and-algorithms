import unittest
from clustering import cluster, minimum_clusters
from file_reader import read_multiple_files
input_files, output_files, assignment, file_path_length = read_multiple_files()


temp = []
inputs_outputs = []
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

class TestCluster(unittest.TestCase):
    def test_cases(self):
        count = 1
        for graph, num_of_nodes, data in inputs_outputs:
            self.assertEqual(cluster(graph, num_of_nodes, k_cluster=4), data)
            print("passed case:", count)
            count += 1


if __name__ == '__main__':
    unittest.main()

# path = os.getcwd() + '/assignment2.txt'

# case = []
# with open(path, 'r') as f:
#     lines = f.readlines()
#     for line in lines[1:]:
#         line = line.replace(" ", "")
#         case.append(line[:-1])

# print(minimum_clusters(case, len(case)))