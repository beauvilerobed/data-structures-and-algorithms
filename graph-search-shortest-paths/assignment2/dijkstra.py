import sys


class Node:
    def __init__(self, value, vertices=None, path_length=None):
        self.value = value
        self.vertices = vertices or []
        self.path_length = path_length or float("inf")
        self.visited = False


class Graph:
    def __init__(self, vertices=None):
        self.vertices = vertices or []

    def print_nodes(self):
        for vertex in self.vertices:
            print("vertex:", vertex.value)
            for vertex in vertex.vertices:
                print("edges:", vertex[0].value, end=",")
            print(" ")


def dijkstra(graph):
    root = graph.vertices[0]
    root.visited = True
    used_paths = {root.value}
    root.path_length = 0
    computed_shortest_path = {root.value}
    n = len(graph.vertices) - 1
    while n > 0:
        minimimize = {}
        chosen_edge = []
        for vertex in graph.vertices:
            if vertex.visited is True:
                for edge in vertex.vertices:
                    if edge[0].value not in used_paths:
                        dijkstra_choice = vertex.path_length + edge[1]
                        minimimize[dijkstra_choice] = [vertex, edge]
        if len(minimimize) == 0:
            break
        minimum = min(list(minimimize.keys()))

        chosen_edge = minimimize[minimum]
        edge = chosen_edge[1][0]
        used_paths.add(edge.value)
        for vertex_in_graph in graph.vertices:
            if vertex_in_graph.value == edge.value:
                vertex_in_graph.visited = True
                vertex_in_graph.path_length = minimum
                computed_shortest_path.add(vertex_in_graph.value)
                break
        n -= 1

    values = []

    for vertex in graph.vertices:
        if vertex.value in {7, 37, 59, 82, 99, 115, 133, 165, 188, 197}:
            values.append(vertex.path_length)
    return values


def main():
    text = sys.stdin.readlines()
    graph = Graph()
    for data in text:
        values = data.split()
        node = Node(int(values[0]))
        edges = values[1:]
        for edge in edges:
            edge_and_length = list(map(int, edge.split(',')))
            edge_node = Node(edge_and_length[0])
            node.vertices.append([edge_node, edge_and_length[1]])

        graph.vertices.append(node)

    dijkstra(graph)


if __name__ == '__main__':
    main()
