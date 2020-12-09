# python3

from file_reader import read_file
import numpy as np
import os
import glob


def floyd_warshal(graph, n):
    A = np.full((n+1, n+1, n+1), float('inf'))
    for i in range(n):
        for j in range(n):
            if i == j:
                A[i, j, 0] = 0
            if (i, j) in graph:
                A[i, j, 0] = graph[i, j]
            else:
                A[i, j, 0] = float('inf')
    
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                A[i, j, k] = min(A[i, j, k-1], A[i, k-1, k-1] + A[k, j, k-1])

    for i in range(1, n+1):
        if A[i,i,n] < 0:
            return 'Null'

    minimum = np.min(A[:,:,n])
    return minimum


def main():
    file_path = os.getcwd() + '/assignments/*'
    paths = glob.glob(file_path)

    graphs = []
    for path in paths:
        graph_data = read_file(path)
        graphs.append(graph_data)

    for graph_data in graphs:
        graph = graph_data[0]
        n = graph_data[1]
        print(floyd_warshal(graph, n))


if __name__ == '__main__':
    main()