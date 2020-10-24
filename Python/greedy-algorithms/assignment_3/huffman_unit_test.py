import os
from huffman import compute_depth

path = os.getcwd() + '/assignment.txt'

case = []
with open(path, 'r') as f:
    lines = f.readlines()
    lines = lines[1:]
    for line in lines:
        case.append(int(line))

print(compute_depth(case))

