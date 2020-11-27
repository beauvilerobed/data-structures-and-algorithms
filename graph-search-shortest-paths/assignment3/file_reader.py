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


def generate_cases(input_files, output_files):
    inputs_outputs = []
    for name1, name2 in zip(input_files, output_files):
        case = []
        with open(name1, 'r') as f:
            lines = f.readlines()
            for line in lines:
                case.append(int(line))

        with open(name2, 'r') as f:
            line = f.readline()
            data = int(line)

        inputs_outputs.append([case, data])

    return inputs_outputs
