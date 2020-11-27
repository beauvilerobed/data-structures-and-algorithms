import copy
import random
import sys
from collections import namedtuple
from math import log2


Edge = namedtuple('Edge', 'vertex vertex_edge')


def do_iter_mincut(graph):
    num_vertexes = len(graph.keys())
    crossing_num = 2 * num_vertexes

    # number of repeated trials is determined by the probablity
    # of output of A & B, the min cut of the graph.
    iterations = num_vertexes ** 2

    for _ in range(iterations):
        graph_copy = copy.deepcopy(graph)
        local_min_crossing_num = compute_mincut(graph_copy)
        if crossing_num > local_min_crossing_num:
            crossing_num = local_min_crossing_num

    return crossing_num


def compute_mincut(graph):
    contracted_graph = rand_contraction(graph)
    for key in contracted_graph:
        return len(contracted_graph[key])


def rand_contraction(graph):
    if len(graph.keys()) <= 2:
        return graph

    edges = return_edges(graph)

    r_edge = random.choice(edges)
    temp = list()
    for edge in r_edge.vertex, r_edge.vertex_edge:
        temp += graph[edge]

    final = compute_final_edges(r_edge, temp)

    del graph[r_edge.vertex]
    del graph[r_edge.vertex_edge]

    new_vertex = update_graph(graph, r_edge)
    graph[new_vertex] = final

    return rand_contraction(graph)


def return_edges(graph):
    edges = []
    for k in graph.keys():
        for e in graph[k]:
            edge = Edge(e, k)
            edges.append(edge)

    return edges


def compute_final_edges(r_edge, temp):
    final = []
    for v in temp:
        if (v != r_edge.vertex) & (v != r_edge.vertex_edge):
            final.append(v)
    
    return final


def update_graph(graph, r_edge):
    new_vertex = r_edge.vertex
    for k in graph.keys():
        new = []
        for edge in graph[k]:
            if (edge == r_edge.vertex) | (edge == r_edge.vertex_edge):
                new.append(new_vertex)
            else:
                new.append(edge)
        graph[k] = new

    return new_vertex


def main():
    data_set = sys.stdin.readlines()
    graph = {}
    for data in data_set:
        values = list(map(int, data.split()))
        vertex = values[0]
        edges = values[1:]
        graph[vertex] = edges
    print(do_iter_mincut(graph))


if __name__ == '__main__':
    main()
