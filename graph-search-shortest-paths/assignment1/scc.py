import copy
import sys


class Node:
    def __init__(self, _id, edges=None):
        self.id = _id
        self.edges = edges or list()
        self.explored = False
        self.finished = False


class Graph:
    def __init__(self):
        self.nodes = dict()

    def reverse(self):
        for node in self.nodes.values():
            node.edges = [-edge for edge in node.edges]
            node.explored = False
            node.finished = False


def find_scc(graph):
    def depth_first_search(node):
        explored = 0
        stack = [node]
        while stack:
            node = stack[-1]
            if node.explored:
                if not node.finished:
                    node.finished = True
                    f.append(stack.pop())
                else:
                    stack.pop()
            else:
                node.explored = True
                explored += 1
                for edge in node.edges:
                    if edge > 0 and not graph.nodes[edge].explored:
                        stack.append(graph.nodes[edge])
        return explored

    def depth_loop(node_order):
        f.clear()
        components = list()
        for node_id in node_order:
            node = graph.nodes[node_id.id]
            if not node.explored:
                components.append(depth_first_search(node))
        return components

    graph.reverse()
    f = list()
    depth_loop(sorted(graph.nodes.values(),
                      key=lambda x: x.id,
                      reverse=True))
    finishing_times = list(reversed(copy.copy(f)))
    graph.reverse()
    components = depth_loop(finishing_times)
    components.extend([0]*5)
    return sorted(components, reverse=True)[:5]


def main():
    data = sys.stdin.readlines()
    graph = Graph()
    for line in data:
        (vertex, edge) = list(map(int, line.split()))
        if vertex not in graph.nodes:
            graph.nodes[vertex] = Node(vertex, edges=[edge])
        else:
            graph.nodes[vertex].edges.append(edge)

        if edge not in graph.nodes:
            graph.nodes[edge] = Node(edge, edges=[-vertex])
        else:
            graph.nodes[edge].edges.append(-vertex)

    print(find_scc(graph))


if __name__ == '__main__':
    main()
