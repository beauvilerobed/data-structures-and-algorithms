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


def generate_inputs_outputs_huff(input_files, output_files):
    inputs_outputs = []
    for name1, name2 in zip(input_files, output_files):
        case = []
        with open(name1, 'r') as f:
            lines = f.readlines()
            lines = lines[1:]
            for line in lines:
                case.append(int(line))

        with open(name2, 'r') as f:
            lines = f.readlines()
            data = list(map(int, lines))

        inputs_outputs.append([case, data])

    return inputs_outputs


def generate_inputs_outputs_max(input_files, output_files):
    inputs_outputs = []
    for name1, name2 in zip(input_files, output_files):
        case = []
        with open(name1, 'r') as f:
            lines = f.readlines()
            for line in lines:
                data = int(line)
                case.append(data)
            length = case[0]

        with open(name2, 'r') as f:
            line = f.readline()[:-1]

        inputs_outputs.append([case, length, line])

    return inputs_outputs
