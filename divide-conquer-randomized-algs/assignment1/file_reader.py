import os
import glob


def generate_files(path='/tests/*'):
    test_case_path = os.getcwd() + path
    files = glob.glob(test_case_path)

    return files


def generate_tests(files):
    cases = []
    for path in files:
        with open(path, 'r') as f:
            lines = f.readlines()
            number_pair = list(map(int, lines))
            cases.append(number_pair)

    return cases
