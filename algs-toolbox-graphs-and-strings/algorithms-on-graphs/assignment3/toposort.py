# python3

# Determining an Order of Courses

# Task. Compute a topological ordering of a given
# directed acyclic graph (DAG) with 𝑛 vertices and
# 𝑚 edges.

import sys


def dfs(adj, used, order, x):
    used[x] = 1
    if len(adj[x]) == 0:
        order.append(x)
    else:
        for neigbor in adj[x]:
            if used[neigbor] == 0:
                dfs(adj, used, order, neigbor)
        order.append(x)


def toposort(adj):
    used = [0] * len(adj)
    order = []
    for i in range(len(adj)):
        if used[i] == 0:
            dfs(adj, used, order, i)

    order.reverse()
    return order


def main():
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')


if __name__ == '__main__':
    main()
