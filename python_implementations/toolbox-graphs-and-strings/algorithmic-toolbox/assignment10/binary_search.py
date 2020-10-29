

def binary_search_naive(keys, query):
    for i in range(len(keys)):
        if keys[i] == query:
            return i
    
    return -1


def binary_search(keys, query):
    low, high = 0, len(keys)
    while low + 1 < high:
        mid = (low + high) // 2
        if keys[mid] <= query:
            low = mid
        else:
            high = mid
    
    if keys[low] != query:
        return -1
    else:
        return low

def main():
    input_keys = list(map(int, input().split()))[1:]
    input_queries = list(map(int, input().split()))[1:]

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')


if __name__ == '__main__':
    main()