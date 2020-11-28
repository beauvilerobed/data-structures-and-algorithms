import os
import glob


def generate_files(path='/tests/*'):
    file_path = os.getcwd() + path
    file_path_length = len(file_path) - 1

    paths = glob.glob(file_path)
    input_files = []
    output_files = []

    for path in paths:
        if path[file_path_length: file_path_length + 5] == 'input':
            input_files.append(path)
        elif path[file_path_length: file_path_length + 6] == 'output':
            output_files.append(path)

    input_files.sort()
    output_files.sort()

    return input_files, output_files


def generate_inputs_outputs(input_files, output_files):
    inputs_outputs = []
    for name1, name2 in zip(input_files, output_files):
        with open(name1, 'r') as f:
            data_set = f.readlines()
            values = []
            info = list(map(int, data_set[0].split()))
            number_items = info[1]
            knapsack_size = info[0]
            for value_pair in data_set[1:]:
                int_values = list(map(int, value_pair.split()))
                values.append(int_values)

        with open(name2, 'r') as f:
            line = f.readline()
            data = int(line)

        inputs_outputs.append([values, number_items, knapsack_size, data])

    return inputs_outputs
