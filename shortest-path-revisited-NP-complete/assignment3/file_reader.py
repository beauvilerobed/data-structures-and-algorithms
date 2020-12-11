# python3 

from itertools import permutations
from collections import namedtuple
from dist import dist


Point = namedtuple('Point', 'x y')


def read_file(file):
    with open(file) as f:
        lines = f.readlines()
        n = int(lines[0])
        cities = {}
        for line in lines[1:]:
            vals = line.split()
            index = int(vals[0])
            coordinates = vals[1:]
            cities[index] = tuple(map(float, coordinates))

        return cities, n

print(read_file('cities.txt')[0])

def get_graph(cities, n):
    graph = {}
    perm = get_perm(n)
    for vals in perm:
        first = vals[0]
        second = vals[1]

        p1 = Point(cities[first][0], cities[first][1])
        p2 = Point(cities[second][0], cities[second][1])
        distance = dist(p1, p2)

        graph[first, second] = distance

    return graph


def get_perm(n):
    nums = [i+1 for i in range(n)]
    perm = permutations(nums, 2)

    return perm
