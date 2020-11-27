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
                lines = f.readlines()
                lines = list(map(lambda x: x.strip(), lines))
                solutions.append(lines)
        else:
            with open(name, 'r') as f:
                line = f.readline().strip()
                cases.append(line)
    
    return cases, solutions
