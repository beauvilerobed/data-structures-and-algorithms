from heapq import heapify, heappush, heappop

# checking if heapify is needed and how heappush handles arrays


def example():
    heap = []
    heappush(heap, [1, 0])
    heappush(heap, [2, -2])
    heappush(heap, [2, 3])
    heappush(heap, [10, -1])
    heappush(heap, [-1, 2])
    heappush(heap, [-199, 1])
    for _ in range(len(heap)):
        print(heappop(heap))


if __name__ == '__main__':
    example()
