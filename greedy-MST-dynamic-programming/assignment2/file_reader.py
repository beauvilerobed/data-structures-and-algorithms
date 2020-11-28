import os
import glob


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


def generate_cases_cluster(input_files, output_files):
    temp = generate_temp(input_files, output_files)
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

    return inputs_outputs


def generate_temp(input_files, output_files):
    temp = []
    for name1, name2 in zip(input_files, output_files):
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

    return temp


def generate_cases_cluster_large(input_files2, output_files2):
    inputs_outputs2 = []
    for name1, name2 in zip(input_files2, output_files2):
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

    return inputs_outputs2
