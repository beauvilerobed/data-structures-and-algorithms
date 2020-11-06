import glob
import errno
import os


def read_files(path="/tests/*"):
    path = os.getcwd() + path
    files = glob.glob(path)
    files.sort()
    return files

def generate_test_cases(files):
    solutions = []
    cases = []
    for name in files:
        with open(name, "r") as f:
            if name[-2:] == ".a":
                line = f.readline()
                solutions.append(line.split()[0])
            else:
                lines = f.readlines()
                test_case = ''
                for line in lines:
                    test_case += line.split()[0]
                cases.append(test_case)
    
    return solutions, cases