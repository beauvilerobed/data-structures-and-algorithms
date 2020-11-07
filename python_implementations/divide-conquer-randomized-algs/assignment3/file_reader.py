import os
import glob
import copy

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


def generate_input_outputs(input_files, output_files, assignment, file_path_length):
    inputs_outputs1 = []
    inputs_outputs2 = []
    inputs_outputs3 = []
    for name1, name2 in zip(input_files, output_files):
        if name1[file_path_length + 5:] != name2[file_path_length + 6:]:
            print("input file", name1[file_path_length + 5:], "is not the same as output file", name2[file_path_length + 6:])
            break
    else:
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