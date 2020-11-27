import os
import glob


def read_multiple_files(path="/tests/*"):
    path = os.getcwd() + path
    files = glob.glob(path)
    files.sort()

    return files


def return_cases(files):
    cases = list()
    solutions = list()
    for name in files:
        if name[-2:] == '.a':
            with open(name, 'r') as f:
                line = f.readline()
                line = list(map(int, line.split()))
                solutions.append(line)
        else:
            with open(name, 'r') as f:
                patterns = f.readlines()
                patterns = list(map(lambda x: x.rstrip('\n'), patterns))
                cases.append(patterns)

    return cases, solutions
