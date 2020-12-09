from collections import namedtuple, defaultdict


def read_file(file):
    graph = defaultdict(list)
    with open(file) as f:
        lines = f.readlines()
        n = int(lines[0].split()[0])
        for line in lines[1:]:
            data = list(map(int, line.split()))
            vertex = data[0]
            edge = data[1]
            edge_len = data[2]
            graph[vertex, edge] = edge_len

        return graph, n