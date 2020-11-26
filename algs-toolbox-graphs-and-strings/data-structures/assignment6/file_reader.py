import glob
import os
from hash_chains import Query


def generate_files(path="/tests/*"):
    path = os.getcwd() + path
    files = glob.glob(path)
    files.sort()
    return files


def generate_test_case(files):
    solution = []
    info = []

    for name in files:
        with open(name, 'r') as f:
            if name[-2:] == ".a":
                lines = f.readlines()
                for line in lines:
                    line = line.rstrip()
                    if len(line) > 0:
                        solution.append(line)
                    else:
                        solution.append('')
            else:
                lines = f.readlines()
                bucket_count = int(lines[0])
                info.append(bucket_count)
                for line in lines[2:]:
                    line = line.rstrip().split()
                    query = Query(line)
                    info.append(query)

    return info, solution
