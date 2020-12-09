# python3 


def read_file(file):
    graph = {}
    with open(file) as f:
        lines = f.readlines()
        n = int(lines[0].split()[0])
        for line in lines[1:]:
            vertex, edge, edge_len = map(int, line.split())
            graph[vertex-1, edge-1] = edge_len

        return graph, n