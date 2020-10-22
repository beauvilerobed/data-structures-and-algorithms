from clustering import cluster, minimum_clusters
import os


# path = os.getcwd() + '/assignment.txt'

# case = []
# with open(path, 'r') as f:
#     lines = f.readlines()
#     for line in lines:
#         line = list(map(int, line.split()))
#         case.append(line)

# graph = {}
# num_of_nodes = case[0][0]
# for vertex, edge, edge_weight in case[1:]:
#     if vertex in graph:
#         graph[vertex].append([edge, edge_weight])
#     else:
#         graph[vertex] = [[edge, edge_weight]]

# print(cluster(graph, num_of_nodes, k_cluster=4))

path = os.getcwd() + '/assignment2.txt'

case = []
with open(path, 'r') as f:
    lines = f.readlines()
    for line in lines[1:]:
        line = line.replace(" ", "")
        case.append(line[:-1])

print(minimum_clusters(case, len(case)))