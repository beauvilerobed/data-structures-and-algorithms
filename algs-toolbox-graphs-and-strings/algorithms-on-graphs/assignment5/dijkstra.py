# python3

# Computing the Minimum Cost of a Flight

# Task. Given an directed graph with positive edge
# weights and with 𝑛 vertices and 𝑚 edges as well as
# two vertices 𝑢 and 𝑣, compute the weight of a
# shortest path between 𝑢 and 𝑣 (that is, the minimum
# total weight of a path from 𝑢 to 𝑣).

import sys
import queue


def distance(adj, cost, s, t):
    num_nodes = float("inf")
    dist = [num_nodes for _ in range(len(adj))]
    prev = [None for _ in range(len(adj))]
    dist[s] = 0
    q = queue.PriorityQueue()
    q.put([0, s])

    while not q.empty():
        u_pair = q.get()
        u = u_pair[1]
        if u == t:
            return dist[u]

        for neighbor, weight in zip(adj[u], cost[u]):
            if dist[neighbor] > dist[u] + weight:
                dist[neighbor] = dist[u] + weight
                prev[neighbor] = u
                q.put([dist[neighbor], neighbor])
    return -1


def main():
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3],
                         data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))


if __name__ == '__main__':
    main()
