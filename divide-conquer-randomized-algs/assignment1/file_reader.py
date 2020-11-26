import os
import glob


def generate_paths(path='/tests/*'):
    test_case_path = os.getcwd() + path
    paths = glob.glob(test_case_path)

    return paths


def generate_tests(paths):
    cases = []
    for path in paths:
        with open(path, 'r') as f:
            lines = f.readlines()
            number_pair = list(map(int, lines))
            cases.append(number_pair)

    return cases
