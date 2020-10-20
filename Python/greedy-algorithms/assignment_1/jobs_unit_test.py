import os
from jobs import scheduling

path = os.getcwd() + '/case2.txt'

case = []
with open(path, 'r') as f:
    lines = f.readlines()
    for line in lines[1:]:
        weight, length = list(map(int, line.split()))
        case.append([weight, length])

print(scheduling(case))
