import os
import glob
from dijkstra import Node, Graph


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


def generate_inputs_outputs(input_files, output_files,
                            assignment, file_path_length):
    inputs_outputs = []
    # TODO: file reading step has nested for loops try to reduce runtime
    for name1, name2 in zip(input_files, output_files):
        if name1[file_path_length+5:] != name2[file_path_length+6:]:
            print("input file", name1[file_path_length+5:],
                  "is not the same as output file", name2[file_path_length+6:])
            break
        else:
            graph = Graph()
            with open(name1, 'r') as f:
                lines = f.readlines()
                for data in lines:
                    values = data.split()
                    node = Node(int(values[0]))
                    edges = values[1:]
                    for edge in edges:
                        edge_and_length = list(map(int, edge.split(',')))
                        edge_node = Node(edge_and_length[0])
                        node.vertices.append([edge_node, edge_and_length[1]])

                    graph.vertices.append(node)

            with open(name2, 'r') as f:
                line = f.readline()
                output_data = list(map(int, line.split(',')))

            inputs_outputs.append([graph, output_data])

    return inputs_outputs
