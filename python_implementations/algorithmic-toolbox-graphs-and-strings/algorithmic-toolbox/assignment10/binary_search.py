

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