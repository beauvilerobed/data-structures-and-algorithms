#Uses python3

# Building Roads to Connect Cities

# Task. Given 𝑛 points on a plane, connect them with 
# segments of minimum total length such that there is 
# a path between any two points.

import sys
import math
import heapq


def prims(x, y):
    nodes_len = len(x)
    result = 0.
    large_num = float("inf")
    cost = [large_num for _ in range(nodes_len)]
    cost[0] = 0
    q = []
    for i in range(nodes_len):
        heapq.heappush(q, [cost[i], i , False])

    while q:
        v_pair = heapq.heappop(q)
        v = v_pair[1]
        for i in range(nodes_len):
            distance_of_points = math.sqrt((x[i] - x[v])**2 + (y[i] - y[v])**2)
            if [cost[i], i] in q and cost[i] > distance_of_points:
                cost[i] = distance_of_points
                heapq.heappush(q, [cost[i], i])
    result = sum(cost)       
    return result


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])
    
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1
        

def kruskal(graph):
    result = []

    i = 0
    e = 0

    graph.graph = sorted(graph.graph, key=lambda item: item[2])
    parent = []
    rank = []

    for node in range(graph.V):
        parent.append(node)
        rank.append(0)
    
    while e < graph.V - 1:
        u ,v ,w = graph.graph[i]
        i += 1
        x = graph.find(parent, u)
        y = graph.find(parent, v)

        if x != y:
            e += 1
            result.append([u, v, w])
            graph.union(parent, rank, x, y)
    total = 0.
    for i in range(len(result)):
        total += result[i][2]
    return total


def main():
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    vertices = list(zip(x,y))
    edges = []
    for i in range(len(vertices)):
        for j in range(len(vertices)):
            if i != j:
                edges.append([i, j, math.sqrt((vertices[i][0] - vertices[j][0])**2 + (vertices[i][1] - vertices[j][1])**2)])
    
    graph = Graph(len(vertices))
    graph.graph = [edge for edge in edges]

    print(n)
    print("{0:.9f}".format(kruskal(graph)))


if __name__ == '__main__':
    main()
