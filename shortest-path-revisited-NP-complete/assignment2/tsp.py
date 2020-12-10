# python3

from itertools import combinations
from file_reader import read_file, get_graph


def tsp(graph, n):
    A = {}

    subsets = get_subsets(n)

    for subset in subsets:
        for j in range(1, n+1):
            if j == 1 and subset == (1,):
                A[subset, j] = 0
            elif j == 1:
                A[subset, j] = float('inf')
            else:
                A[subset, j] = None
    
    for m in range(2, n+1):
        for subset in subsets:
            if len(subset) == m:
                for j in subset:
                    if j != 1:

                        values = []
                        for k in subset:
                            if k != j:
                                edge_len = graph[k, j]
                                new_subset = subtract(subset, (j,))
                                values.append(A[new_subset, k] + edge_len)
                        
                        A[subset, j] = min(values)
    
    minimum = float('inf')
    s_len = len(subsets)
    final_subset = subsets[s_len-1]
    for j in range(2, n+1):
        edge_len = graph[j, 1]
        if A[final_subset, j] + edge_len < minimum:
            minimum = A[final_subset, j] + edge_len

    return int(minimum)


def subtract(subset, singleton):
    subset_list = list(subset)
    value = singleton[0]
    subset_list.remove(value)
    new_subset = tuple(subset_list)

    return new_subset


def get_subsets(n):
    nums = [i + 1 for i in range(n)]
    perms = []
    for i in range(1, n):
        perms.extend(combinations(nums[1:], i))

    subsets = [(1,)]
    for nums in perms:
        subsets.append((1,) + nums)

    return subsets


def main():
    cities, n = read_file('cities.txt')
    graph = get_graph(cities, n)
    print(tsp(graph, n) == 7)


if __name__ == '__main__':
    main()
    