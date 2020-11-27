import os
import glob
import copy


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
    inputs_outputs1 = []
    inputs_outputs2 = []
    inputs_outputs3 = []
    for name1, name2 in zip(input_files, output_files):
        with open(name1, 'r') as f:
            lines = f.readlines()
            input_data1 = list(map(int, lines))
            input_data2 = copy.copy(input_data1)
            input_data3 = copy.copy(input_data1)

        with open(name2, 'r') as f:
            lines = f.readlines()
            output_data1 = list(map(int, lines))
            output_data2 = copy.copy(output_data1)
            output_data3 = copy.copy(output_data1)

            inputs_outputs1.append([input_data1, output_data1])
            inputs_outputs2.append([input_data2, output_data2])
            inputs_outputs3.append([input_data3, output_data3])

    return inputs_outputs1, inputs_outputs2, inputs_outputs3
