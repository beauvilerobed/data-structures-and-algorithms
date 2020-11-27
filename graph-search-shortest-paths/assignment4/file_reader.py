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


def generate_cases(input_files, output_files):
    cases = []
    for name1, name2 in zip(input_files, output_files):
        with open(name1, 'r') as f:
            lines = f.readlines()
            case = list(map(int, lines))

        with open(name2, 'r') as f:
            line = f.readline()
            data = int(line)

        cases.append([case, data])
        print("finished processing file", len(cases))

    return cases
