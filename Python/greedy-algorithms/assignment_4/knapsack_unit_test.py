import os
from knapsack import knapsack, knapsack_fast

path = os.getcwd() + '/small.txt'

case = []
with open(path, 'r') as f:
    lines = f.readlines()
    for line in lines[1:]:
        data = list(map(int, line.split()))
        case.append(data)

line = lines[0].split()
data = list(map(int, line))
num_items = data[1]
knapsack_size = data[0]

print(knapsack(case, num_items, knapsack_size))