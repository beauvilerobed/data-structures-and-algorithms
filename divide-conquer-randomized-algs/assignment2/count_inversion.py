import sys


def sort_count(array, arraylen):
    if arraylen == 1:
        return [array, 0]

    half = arraylen // 2
    first_half = array[:half]
    second_half = array[half:]

    firstsort_count = sort_count(first_half, len(first_half))
    secondsort_count = sort_count(second_half, len(second_half))
    merge_count = count_split_inv(firstsort_count[0],
                                  secondsort_count[0],
                                  arraylen)

    return [merge_count[0], merge_count[1] +
            firstsort_count[1] + secondsort_count[1]]


def count_split_inv(array1, array2, sumlen):
    result = []
    count = 0
    for _ in range(sumlen):
        if len(array1) == 0 or len(array2) == 0:
            result.extend(array1)
            result.extend(array2)
            break
        if array1[0] < array2[0]:
            result.append(array1.pop(0))
        else:
            count += len(array1)
            result.append(array2.pop(0))

    return [result, count]


def main():
    data = sys.stdin.read()
    data_set = list(map(int, data.split()))
    print(sort_count(data_set, len(data_set))[1])


if __name__ == '__main__':
    main()
