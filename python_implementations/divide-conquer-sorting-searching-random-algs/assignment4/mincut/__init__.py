import copy
import random

def  do_thirty_iter_mincut(graph):
  num_vertexes = len(graph.keys())
  crossing_edges = 2 * num_vertexes

  iterate = 50
  minimum_cut = graph

  while iterate > 0:
    new_graph = copy.deepcopy(graph)
    local_minimum = compute_mincut(new_graph)
    vertex_keys = list(local_minimum.keys())
    local_min_crossing_edges = len(local_minimum[vertex_keys[0]])
    if crossing_edges > local_min_crossing_edges:
      crossing_edges = local_min_crossing_edges
      minimum_cut = local_minimum
    
    iterate = iterate - 1

  return crossing_edges

def compute_mincut(graph):
  if len(graph.keys()) <= 2:
    return graph

  edges = []
  
  for k in graph.keys():
    for e in graph[k]:
      edge = [k, e]
      edges.append(edge)

  random_edge = random.choice(edges)
  vertex = random_edge[0]
  vertex_to_merge = random_edge[1]
  edges_of_graph_vertex = graph[vertex]

  merge_vertex_name = vertex
  edges_of_graph_merge_vertex = graph[vertex_to_merge]
 
  penultimate_edges = edges_of_graph_vertex + edges_of_graph_merge_vertex
  final_edges = []

  for v in penultimate_edges:
    if (v != vertex) & (v != vertex_to_merge):
      final_edges.append(v)
  
  del graph[vertex]
  del graph[vertex_to_merge]

  for k in graph.keys():
    temp_edges = []
    for edge in graph[k]:
      if (edge == vertex) | (edge == vertex_to_merge):
        temp_edges.append(merge_vertex_name)
      else:
        temp_edges.append(edge)

    graph[k] = temp_edges

  graph[merge_vertex_name] = final_edges

  return compute_mincut(graph)

