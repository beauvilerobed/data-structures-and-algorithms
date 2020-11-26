import sys
from heapq import heappush, heappop

sys.setrecursionlimit(100000)


class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


def compute_depth(weights):
    def huffman(weights_heap):
        if len(weights_heap) == 2:
            node = Node(None)
            node.right = weights_heap[0][2]
            node.left = weights_heap[1][2]
            return node

        weight1 = heappop(weights_heap)
        weight2 = heappop(weights_heap)
        new_weight = weight1[0] + weight2[0]
        new_node = Node(None)
        new_index = str(weight1[1]) + str(weight2[1])
        new_node.left = weight1[2]
        new_node.right = weight2[2]
        heappush(weights_heap, [new_weight, new_index, new_node])
        node = huffman(weights_heap)

        return node

    def find_depth_min(node):
        if node.left is None and node.right is None:
            return 0

        return 1 + min(find_depth_min(node.left), find_depth_min(node.right))

    def find_depth_max(node):
        if node.left is None and node.right is None:
            return 0

        return 1 + max(find_depth_max(node.left), find_depth_max(node.right))

    weights_heap = []
    for i in range(len(weights)):
        node = Node(i)
        heappush(weights_heap, [weights[i], str(node.value), node])
    node = huffman(weights_heap)
    return [find_depth_max(node), find_depth_min(node)]


def main():
    data = sys.stdin.read()
    data_set = list(map(int, data.split()))
    print(compute_depth(data_set[1:]))


if __name__ == '__main__':
    main()
