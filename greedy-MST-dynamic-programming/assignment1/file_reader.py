import os
import glob


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


def generate_inputs_outputs_prim(input_files, output_files,
                                 assignment, file_path_length):

    temp = generate_temp_cases(input_files, output_files,
                               assignment, file_path_length)

    inputs_outputs = []
    for input_output in temp:
        case = input_output[0]
        data = input_output[1]
        graph = {}
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
        inputs_outputs.append([graph, data])

    return inputs_outputs


def generate_temp_cases(input_files, output_files,
                        assignment, file_path_length):
    temp = []
    for name1, name2 in zip(input_files, output_files):
        if name1[file_path_length + 5:] != name2[file_path_length + 6:]:
            print("input file", name1[file_path_length+5:],
                  "is not the same as output file", name2[file_path_length+6:])
            break
        else:
            case = []
            with open(name1, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    data = list(map(int, line.split()))
                    case.append(data)
            with open(name2, 'r') as f:
                line = f.readline()
                data = int(line)

            temp.append([case, data])
    return temp


def generate_inputs_outputs_jobs(input_files, output_files,
                                 assignment, file_path_length):
    inputs_outputs = []
    for name1, name2 in zip(input_files, output_files):
        if name1[file_path_length + 5:] != name2[file_path_length + 6:]:
            print("input file", name1[file_path_length+5:],
                  "is not the same as output file", name2[file_path_length+6:])
            break
        else:
            case = []
            with open(name1, 'r') as f:
                lines = f.readlines()
                for line in lines[1:]:
                    weight, length = list(map(int, line.split()))
                    case.append([weight, length])
            with open(name2, 'r') as f:
                lines = f.readlines()
                data = list(map(int, lines))

            inputs_outputs.append([case, data])

    return inputs_outputs
