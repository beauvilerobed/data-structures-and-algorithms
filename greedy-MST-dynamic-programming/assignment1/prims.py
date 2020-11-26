import sys


def prims(graph, length):
    root = 1
    chosen_vertices = [root]
    added_edges = []

    while len(chosen_vertices) < length:
        cheapest_edge = float("inf")
        chosen_edge = [0, 0, 0]
        for vertex in chosen_vertices:
            for edge_pair in graph[vertex]:
                edge_value = edge_pair[0]
                edge_weight = edge_pair[1]
                is_not_in_vertices = edge_value not in chosen_vertices
                is_less_cheapest_edge = edge_weight < cheapest_edge
                if is_not_in_vertices and is_less_cheapest_edge:
                    cheapest_edge = edge_weight
                    chosen_edge = [edge_value, vertex, edge_weight]

        edge_value, _, edge_weight = chosen_edge
        added_edges.append(edge_weight)
        chosen_vertices.append(edge_value)

    cost = sum(added_edges)
    return cost


def main():
    data = sys.stdin.read()
    data_set = list(map(int, data.split()))
    length = data_set[0]
    data_set = [[data_set[i], data_set[i + 1], data_set[i + 2]]
                for i in range(2, len(data_set), 3)]
    graph = {}
    for value in data_set:
        vertex = value[0]
        edge = value[1:]
        if vertex in graph:
            graph[vertex].append(edge)
        else:
            graph[vertex] = [edge]

    print(prims(graph, length))


if __name__ == '__main__':
    main()
