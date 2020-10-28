

def compute_min_num_of_refills(d, m, stops):
    stops = [0] + stops + [d]
    n = len(stops)
    num_refill, current_refill = 0, 0
    while current_refill < n - 1:
        last_refill = current_refill
        while (current_refill < n - 1) and (stops[current_refill + 1] - stops[last_refill] <= m):
            current_refill += 1
        if current_refill == last_refill:
            return -1
        if current_refill < n - 1:
            num_refill += 1
    
    return num_refill


if __name__ == '__main__':
    input_d = int(input())
    input_m = int(input())
    input_stops = list(map(int, input().split()))

    print(compute_min_num_of_refills(input_d, input_m, input_stops))