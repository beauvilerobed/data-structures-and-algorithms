import glob
import os


def generate_files(path='/tests/*'):
    path = os.getcwd() + path
    files = glob.glob(path)
    files.sort()
    return files


def generate_test_case(files):
    solution = []

    for name in files:
        with open(name, "r") as f:
            if name[-2:] == ".a":
                lines = f.readlines()
                solution = []
                for line in lines:
                    solution.append(list(map(int, line.split())))
            else:
                lines = f.readlines()
                lines = lines[1:]
                test_case = []
                for line in lines:
                    case = list(map(int, line.split()))
                    test_case.extend(case)

    return solution, test_case
