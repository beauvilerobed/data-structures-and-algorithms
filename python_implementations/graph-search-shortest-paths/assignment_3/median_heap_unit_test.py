import os
from median_heap import median_heap

path = os.getcwd() + '/case.txt'

case = []
with open(path, 'r') as f:
    lines = f.readlines()
    for line in lines:
        case.append(int(line))

print(median_heap(case) % 10000)