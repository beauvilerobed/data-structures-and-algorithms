import os
from max_weight_IS import max_weight_IS

path = os.getcwd() + '/assignment2.txt'

case = []
with open(path, 'r') as f:
    lines = f.readlines()
    for line in lines:
        data = int(line)
        case.append(data)
length = case[0]
print(max_weight_IS(case[1:], length))