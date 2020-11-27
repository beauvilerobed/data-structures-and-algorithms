import os
import glob


def generate_files(path='/tests/*'):
    files = os.getcwd() + path
    len_files = len(files) - 1

    paths = glob.glob(files)
    input_files = []
    output_files = []

    for path in paths:
        if path[len_files: len_files + 5] == 'input':
            input_files.append(path)
        elif path[len_files: len_files + 6] == 'output':
            output_files.append(path)

    input_files.sort()
    output_files.sort()

    return input_files, output_files, len_files


def generate_cases(input_files, output_files, len_files):
    inputs_outputs = []
    for name1, name2 in zip(input_files, output_files):
            with open(name1, 'r') as f:
                graph = {}
                lines = f.readlines()
                for line in lines:
                    values = list(map(int, line.split()))
                    vertex = values[0]
                    edges = values[1:]
                    graph[vertex] = edges

            with open(name2, 'r') as f:
                line = f.readline()
                value = int(line)

            inputs_outputs.append([graph, value])

    return inputs_outputs
