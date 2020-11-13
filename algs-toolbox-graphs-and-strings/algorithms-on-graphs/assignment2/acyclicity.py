#Uses python3
import sys

# Checking Consistency of CS Curriculum

# Task. Check whether a given directed graph with 𝑛 
# vertices and 𝑚 edges contains a cycle.


def acyclic(adj):
    def explore(vertex, nodes):
        visited[vertex] = True
        nodes.append(vertex)

        for neighbor in adj[vertex]:
            if neighbor in nodes:
                result[0] = 1

            if not visited[neighbor]:
                explore(neighbor, nodes)
                nodes.pop()
            
    result = [0]
    visited = [False for _ in range(len(adj))]

    for i in range(len(adj)):
        if not visited[i]:
            explore(i, [])
    return result[0]


def main():
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))


if __name__ == '__main__':
    main()
