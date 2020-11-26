import sys
import itertools
import copy


class Subset:
    def __init__(self, parent, rank):
        self.parent = parent
        self.rank = rank


def find(subsets, node):
    while subsets[node].parent != node:
        node = subsets[node].parent
    return node


def union(subsets, u, v):
    u = find(subsets, u)
    v = find(subsets, v)
    if u == v:
        return False
    if subsets[u].rank > subsets[v].rank:
        subsets[v].parent = u
        return v
    else:
        subsets[u].parent = v
        if subsets[u].rank == subsets[v].rank:
            subsets[v].rank += 1
        return u


def cluster(graph, number_of_nodes, k_cluster):
    edges = []
    for vertex in graph:
        for edge in graph[vertex]:
            edge_value = edge[0]
            edge_weight = edge[1]
            edges.append([vertex, edge_value, edge_weight])
    edges.sort(key=lambda x: x[2])

    leaders = [i for i in range(number_of_nodes + 1)]
    clusters = [Subset(i, 0) for i in range(number_of_nodes + 1)]

    spacing = []
    number_of_leaders = len(leaders) - 1
    while number_of_leaders >= k_cluster:
        vertex, edge_value, edge_weight = edges.pop(0)
        leader_to_remove = union(clusters, vertex, edge_value)
        if leader_to_remove and leaders[leader_to_remove - 1] != -1:
            spacing.append(edge_weight)
            number_of_leaders -= 1
            leaders[leader_to_remove - 1] = -1
    return spacing[-1]


def largest_clusters(vertices, num_of_vertices, spacing=2):
    leaders = {}

    for i, vertex in enumerate(vertices):
        leaders[vertex] = i + 1

    leader_board = [i for i in range(num_of_vertices + 1)]
    clusters = [Subset(i, 0) for i in range(num_of_vertices + 1)]
    number_of_leaders = len(leaders)
    for i in range(1, spacing + 1):
        for vertex in vertices:
            within_spacing = hamming_possibilies(vertex, i)
            for neighber in within_spacing:
                if neighber in leaders:
                    if find(clusters, leaders[vertex]) ==\
                       find(clusters, leaders[neighber]):
                        continue
                    leader_to_remove =\
                        union(clusters, leaders[vertex], leaders[neighber])
                    if leader_board[leader_to_remove] != 0:
                        number_of_leaders -= 1
                        leader_board[leader_to_remove] = 0
    return number_of_leaders


def switch(bit):
    if bit == 1:
        return 0
    return 1


def hamming_possibilies(vertex, distance):
    coordinates = itertools.combinations(range(len(vertex)), distance)
    vertex = [letter for letter in vertex]
    vertices = list()
    for coordinate in coordinates:
        new_vertex = copy.copy(vertex)
        for index in coordinate:
            bit = int(vertex[index])
            new_vertex[index] = str(switch(bit))
        new_vertex = "".join(new_vertex)
        vertices.append(new_vertex)

    return vertices


def main():
    data = sys.stdin.read()
    data_set = list(map(int, data.split()))
    num_of_nodes = data_set[0]
    graph = {}
    for i in range(1, num_of_nodes, 3):
        vertex = data_set[i]
        edge = data_set[i + 1]
        edge_weight = data_set[i + 2]
        if vertex in graph:
            graph[vertex].append([edge, edge_weight])
        else:
            graph[vertex] = [[edge, edge_weight]]

    print(cluster(graph, num_of_nodes, k_cluster=4))

if __name__ == '__main__':
    main()
