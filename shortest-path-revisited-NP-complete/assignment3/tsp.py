# python3

from file_reader import read_file, get_graph
from dist import dist


def tsp(graph, n):
    visited = [1]
    distance = 0

    while len(visited) < n:
        unvisited = set(range(1, n+1)) - set(visited)
        index = visited[-1]
        minimum, j = min([(graph[index, j], j) for j in unvisited])
        distance += minimum
        visited.append(j)
    
    return int(distance + graph[visited[-1], 1])


def main():
    cities, n = read_file('cities.txt')
    graph = get_graph(cities, n)
    print(tsp(graph, n) == 23)


if __name__ == '__main__':
    main()
    