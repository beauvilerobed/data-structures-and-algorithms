import os
import glob
from dijkstra import Node, Graph


def generate_files(file='/tests/*'):
    file_file = os.getcwd() + file
    len_file = len(file_file) - 1

    files = glob.glob(file_file)
    input_files = []
    output_files = []

    for file in files:
        if file[len_file: len_file + 5] == 'input':
            input_files.append(file)
        elif file[len_file: len_file + 6] == 'output':
            output_files.append(file)

    input_files.sort()
    output_files.sort()

    return input_files, output_files, len_file


def generate_cases(input_files, output_files):
    cases = []
    for name1, name2 in zip(input_files, output_files):
        graph = Graph()
        with open(name1, 'r') as f:
            lines = f.readlines()
            for data in lines:
                values = data.split()
                node = Node(int(values[0]))
                edges = values[1:]
                for edge in edges:
                    edge, edge_len = list(map(int, edge.split(',')))
                    edge_node = Node(edge)
                    node.vertices.append([edge_node, edge_len])

                graph.vertices.append(node)

        with open(name2, 'r') as f:
            line = f.readline()
            output_data = list(map(int, line.split(',')))

        cases.append((graph, output_data))
        print("finished processing file:", len(cases))

    return cases
