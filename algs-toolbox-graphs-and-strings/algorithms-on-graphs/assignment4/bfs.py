# python3

# Computing the Minimum Number of Flight Segments

# Task. Given an undirected graph with 𝑛 vertices and
# 𝑚 edges and two vertices 𝑢 and 𝑣, compute the
# length of a shortest path between 𝑢 and 𝑣 (that is,
# the minimum number of edges in a path from 𝑢 to 𝑣).

import sys
import queue


def distance(adj, s, t):
    num_nodes = len(adj)
    dist = [num_nodes for _ in range(num_nodes)]
    dist[s] = 0
    q = queue.Queue()
    q.put(s)
    result = -1
    while not q.empty():
        u = q.get()
        if u == t:
            result = dist[u]
            break

        for neighbor in adj[u]:
            if dist[neighbor] == num_nodes:
                q.put(neighbor)
                dist[neighbor] = dist[u] + 1

    return result


def main():
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))


if __name__ == '__main__':
    main()
