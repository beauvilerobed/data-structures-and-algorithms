import sys
from heapq import heapify, heappop, heappush

def median_heap(values):
    low = []
    heapify(low)
    high = []
    heapify(high)

    heappush(low, -1 * values[0])
    m_total = values[0]

    for i in range(1, len(values)):
        heap_max_value = -1 * low[0]
        if heap_max_value > values[i]:
            heappush(low, -1 * values[i])
        else:
            heappush(high, values[i])

        if len(low) < len(high):
            heap_min_value = heappop(high)
            heappush(low,  -1 * heap_min_value)
        elif len(high) + 1 < len(low):
            heap_max_value = heappop(low)
            heappush(high, -1 * heap_max_value)
        
        m_total += -1 * low[0]
    
    return m_total % 10000


def main():
    text = sys.stdin.read()
    data_set = list(map(int, text.split()))
    median_heap(data_set)


if __name__ == '__main__':
    main()
    