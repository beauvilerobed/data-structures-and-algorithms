import os
from two_sums import find_two_sum_total

path = os.getcwd() + '/case.txt'

case = []
with open(path, 'r') as f:
    lines = f.readlines()
    for line in lines:
        case.append(int(line))

targets = [i for i in range(-10000, 10001)]
count = find_two_sum_total(case, targets)
print(count)