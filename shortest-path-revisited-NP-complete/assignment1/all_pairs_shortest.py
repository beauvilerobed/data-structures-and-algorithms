# python3

from file_reader import read_file
import numpy as np
import os
import glob


def floyd_warshal(graph, n):
    A = np.full((n, n), float('inf'))
    for i in range(n):
        for j in range(n):
            if i == j:
                A[i, j] = 0
            if (i, j) in graph:
                A[i, j] = graph[i, j]
            if i != j and (i, j) not in graph:
                A[i, j] = float('inf')
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                A[i, j] = min(A[i, j], A[i, k] + A[k, j])

    for i in range(n):
        if A[i,i] < 0:
            return 'Null'

    np.fill_diagonal(A, np.inf)
    return A.min()


def main():
    file_path = os.getcwd() + '/files/*'
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