# python3

# Finding an Exit from a Maze

# Task. Given an undirected graph and two distinct
# vertices 𝑢 and 𝑣, check if there is a path between
# 𝑢 and 𝑣.

import sys


def reach(adj, x, y):
    def explore(vertex):
        visited[vertex] = True
        if vertex == y:
            result.append(1)
        for neighbor in adj[vertex]:
            if not visited[neighbor]:
                explore(neighbor)

    visited = [False for _ in range(len(adj))]
    result = [0]
    explore(x)
    return result[-1] or 0


def main():
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(reach(adj, x, y))


if __name__ == '__main__':
    main()
