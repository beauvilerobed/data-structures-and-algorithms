import glob
import os
from tree_orders import TreeOrders


def generate_files(path="/tests/*"):
    path = os.getcwd() + path
    files = glob.glob(path)
    files.sort()
    return files


def generate_test_case(files):
    solutions = []
    trees = []

    for name in files:
        with open(name, 'r') as f:
            if name[-2:] == ".a":
                lines = f.readlines()
                temp = []
                for line in lines:
                    line = line.rstrip()
                    temp.append(line)
                solutions.append(temp)

            else:
                lines = f.readlines()
                trees.append(lines)

    for i in range(len(trees)):
        tree = TreeOrders()
        lines = trees[i]
        n = int(lines[0].rstrip())
        key = [0] * n
        left = [0] * n
        right = [0] * n
        for j in range(n):
            [a, b, c] = map(int, lines[1:][j].split())
            key[j] = a
            left[j] = b
            right[j] = c

        tree.read(n, key, left, right)
        trees[i] = tree

    return trees, solutions
