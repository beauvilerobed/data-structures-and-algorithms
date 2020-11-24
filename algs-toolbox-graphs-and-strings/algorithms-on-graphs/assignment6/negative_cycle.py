#Uses python3

# Detecting Anomalies in Currency Exchange Rates

# Task. Given an directed graph with possibly 
# negative edge weights and with 𝑛 vertices and 𝑚 
# edges, check whether it contains a cycle of 
# negative weight.

import sys
import queue


def negative_cycle(adj, cost):
    for s in range(len(adj)):
        largest = float("inf")
        dist = [largest for _ in range(len(adj))]
        prev = [None for _ in range(len(adj))]
        dist[s] = 0

        for i in range(len(adj)):
            if dist[s] < 0:
                return 1
            for neighbor, weight in zip(adj[i], cost[i]):
                if dist[neighbor] > dist[i] + weight:
                    dist[neighbor] = dist[i] + weight
                    prev[neighbor] = i                   
    return 0


def main():
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    print(negative_cycle(adj, cost))


if __name__ == '__main__':
    main()
