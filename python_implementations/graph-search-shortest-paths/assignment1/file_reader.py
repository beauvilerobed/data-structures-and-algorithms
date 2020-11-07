import os
import glob
from scc import Node, Graph, find_scc

def generate_files(path='/tests/*'):
    file_path = os.getcwd() + path
    file_path_length = len(file_path) - 1

    paths = glob.glob(file_path)
    input_files = []
    output_files = []
    assignment = ''

    for path in paths:
        if path[file_path_length: file_path_length + 5] == 'input':
            input_files.append(path)
        elif path[file_path_length: file_path_length + 6] == 'output':
            output_files.append(path)
        else:
            assignment = path

    input_files.sort()
    output_files.sort()

    return input_files, output_files, assignment, file_path_length

def generate_inputs_outputs(input_files, output_files, assignment, file_path_length):
    inputs_outputs = []
    # TODO: file reading step has a nested for loops, try to reduce runtime
    for name1, name2 in zip(input_files, output_files):
        if name1[file_path_length + 5:] != name2[file_path_length + 6:]:
            print("input file", name1[file_path_length + 5:], "is not the same as output file", name2[file_path_length + 6:])
            break
        else:
            graph = Graph()
            with open(name1, 'r') as f:
                for line in f.readlines():
                    (_id, connecting_vertex) = (int(i) for i in line.split(' ', 1))
                    if _id not in graph.nodes:
                        graph.nodes[_id] = Node(_id, edges=[connecting_vertex])
                    else:
                        graph.nodes[_id].edges.append(connecting_vertex)
                    
                    if connecting_vertex not in graph.nodes:
                        graph.nodes[connecting_vertex] = Node(connecting_vertex, edges=[-_id])
                    else:
                        graph.nodes[connecting_vertex].edges.append(-_id)

            with open(name2, 'r') as f:
                line = f.readline()
                data = list(map(int, line.split(',')))

            inputs_outputs.append([graph, data])
            print("finished processing file number", len(inputs_outputs))

    return inputs_outputs