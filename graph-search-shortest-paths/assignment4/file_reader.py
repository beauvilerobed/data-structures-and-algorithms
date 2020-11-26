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


def generate_inputs_outputs(input_files, output_files,
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
                for line in lines:
                    case.append(int(line))

            with open(name2, 'r') as f:
                line = f.readline()
                data = int(line)

            inputs_outputs.append([case, data])

    return inputs_outputs
