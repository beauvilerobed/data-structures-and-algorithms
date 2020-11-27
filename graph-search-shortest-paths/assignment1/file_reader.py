import os
import glob
from scc import Node, Graph, find_scc


def generate_files(path='/tests/*'):
    file_path = os.getcwd() + path
    len_file = len(file_path) - 1

    paths = glob.glob(file_path)
    input_files = []
    output_files = []

    for path in paths:
        if path[len_file: len_file + 5] == 'input':
            input_files.append(path)
        elif path[len_file: len_file + 6] == 'output':
            output_files.append(path)

    input_files.sort()
    output_files.sort()

    return input_files, output_files


def generate_cases(input_files, output_files):
    inputs_outputs = []
    for name1, name2 in zip(input_files, output_files):
        graph = Graph()
        with open(name1, 'r') as f:
            for line in f.readlines():
                vertex, edge = list(map(int, line.split()))
                if vertex not in graph.nodes:
                    graph.nodes[vertex] = Node(vertex, edges=[edge])
                else:
                    graph.nodes[vertex].edges.append(edge)

                if edge not in graph.nodes:
                    graph.nodes[edge] = Node(edge, edges=[-vertex])
                else:
                    graph.nodes[edge].edges.append(-vertex)

        with open(name2, 'r') as f:
            line = f.readline()
            data = list(map(int, line.split(',')))

        inputs_outputs.append([graph, data])
        print("finished processing file number", len(inputs_outputs))

    return inputs_outputs
