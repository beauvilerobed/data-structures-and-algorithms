# python3

# Convert array into heap

# Task. The first step of the HeapSort algorithm is to create a
# heap from the array you want to sort. By the way, did you know
# that algorithms based on Heaps are widely used for external
# sort, when you need to sort huge files that don’t fit into
# memory of a computer?

# Your task is to implement this first step and convert a given
# array of integers into a heap. You will do that by applying a
# certain number of swaps to the array. Swap is an operation
# which exchanges elements 𝑎𝑖 and 𝑎𝑗 of the array 𝑎 for some 𝑖and 𝑗.
# You will need to convert the array into a heap using only 𝑂(𝑛)
# swaps, as was described in the lectures. Note that you will
# need to use a min-heap instead of a max-heap in this problem.

import math


def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """

    def sift_down(index):
        max_index = index
        left = left_child(index)
        if left < size and data[left] < data[max_index]:
            max_index = left

        right = right_child(index)
        if right < size and data[right] < data[max_index]:
            max_index = right

        if index != max_index:
            data[index], data[max_index] = data[max_index], data[index]
            swaps.append([index, max_index])
            sift_down(max_index)

    size = len(data)
    swaps = []
    half_size = math.floor(size / 2)
    for i in reversed(range(half_size)):
        sift_down(i)

    return swaps


def left_child(index):
    return 2 * index + 1


def right_child(index):
    return 2 * (index + 1)


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
