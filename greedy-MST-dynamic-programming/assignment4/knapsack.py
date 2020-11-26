import sys
import copy


def knapsack(values, number_items, knapsack_size):
    a = [[0 for _ in range(knapsack_size + 1)] for _ in range(number_items)]

    for i in range(number_items):
        for x in range(knapsack_size + 1):
            value = values[i][0]
            weight = values[i][1]
            if weight > x:
                a[i][x] = a[i-1][x]
            else:
                a[i][x] = max(a[i-1][x], a[i-1][x - weight] + value)

    return a[number_items-1][knapsack_size]


def knapsack_fast(values, number_items, knapsack_size):
    a = [0 for _ in range(knapsack_size + 1)]
    b = [0 for _ in range(knapsack_size + 1)]
    # intervals = [i for i in range(0, number_items + 1, 100)]
    for i in range(number_items):
        weight = values[i][1]
        b[:weight] = a[:weight]

        for x in range(weight, knapsack_size + 1):
            value = values[i][0]
            not_added = a[x]
            added = a[x - weight] + value
            if added > not_added:
                b[x] = added
        a = copy.copy(b)

    return a[-1]


def main():
    data = sys.stdin.read()
    data_set = data.split()
    values = []
    info = list(map(int, data_set[0].split()))
    number_items = info[1]
    knapsack_size = info[0]
    for values in data_set[1:]:
        int_values = list(map(int, values.split()))
        values.append(int_values)

    print("knapsack:", knapsack(values, number_items, knapsack_size))
    print("knapsack fast:", knapsack_fast(values, number_items, knapsack_size))


if __name__ == '__main__':
    main()
