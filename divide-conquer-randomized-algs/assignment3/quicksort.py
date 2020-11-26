import sys


def quicksort(input_array, array_len):
    if array_len == 1:
        return input_array

    pivot = choose_pivot(input_array)
    partition = partition_around_array(input_array, pivot)

    first_partition = quicksort(partition[0], len(partition[0]))
    second_partition = quicksort(partition[1], len(partition[1]))

    return first_partition + second_partition


def choose_pivot(input_array):
    return input_array[0]


def partition_around_array(input_array, pivot):
    i = 1
    for j in range(1, len(input_array)):
        if input_array[j] < pivot:
            input_array[i], input_array[j] = input_array[j], input_array[i]
            i += 1

    input_array[i-1], input_array[0] = input_array[0], input_array[i-1]

    if i == 1:
        i = 2

    return input_array[:i-1], input_array[i-1:]


def main():
    data = sys.stdin.read()
    data_set = list(map(int, data.split()))
    print(quicksort(data_set, len(data_set)))


if __name__ == '__main__':
    main()
