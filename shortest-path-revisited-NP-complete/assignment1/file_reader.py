from collections import namedtuple

Edge = namedtuple('Edge', 'edge value')


def read_file(file):
    graph = {}
    with open(file) as f:
        lines = f.readlines()
        n = int(lines[0].split()[0])
        for line in lines[1:]:
            data = list(map(int, line.split()))
            vertex = data[0]
            edge = Edge(data[1], data[2])
            graph[vertex] = edge

        return graph, n