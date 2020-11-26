import glob
import os

from collections import namedtuple

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])


def generate_files(path="/tests/*"):
    path = os.getcwd() + path
    files = glob.glob(path)
    files.sort()
    return files


def generate_test_cases(files):
    solutions = []
    test_cases = []

    for name in files:
        with open(name, "r") as f:
            if name[-2:] == ".a":
                lines = f.readlines()
                temp = []
                for line in lines:
                    solution_list = list(map(int, line.split()))
                    solution = AssignedJob(solution_list[0], solution_list[1])
                    temp.append(solution)
                solutions.append(temp)
            else:
                lines = f.readlines()
                temp = []
                elements = list(map(int, lines[0].split()))
                temp.append(elements[0])
                for line in lines[1:]:
                    partial = list(map(int, line.split()))
                    temp.extend(partial)
                test_cases.append(temp)

    return solutions, test_cases
