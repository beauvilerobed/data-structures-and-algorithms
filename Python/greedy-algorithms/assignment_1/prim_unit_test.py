import os
from prims import prims

path = os.getcwd() + '/case2.txt'

case = []
with open(path, 'r') as f:
    lines = f.readlines()
    for line in lines:
        data = list(map(int, line.split()))
        case.append(data)




graph = {}
length = case[0][0]
for value in case[1:]:
    vertex = value[0]
    edge = value[1]
    edge_value = value[2]
    if vertex in graph:
        graph[vertex].append([edge, edge_value])
    else:
        graph[vertex] = [[edge, edge_value]]

    if edge != vertex:
        if edge in graph:
            graph[edge].append([vertex, edge_value])
        else:
            graph[edge] = [[vertex, edge_value]]
        
print(graph)
# print(prims(graph, length) == -3612829)