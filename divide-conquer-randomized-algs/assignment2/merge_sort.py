def merge_sort(array, arraylen):
    if arraylen == 1:
        return array

    half = arraylen // 2
    first_half = array[:half]
    second_half = array[half:]

    first_sorted = merge_sort(first_half, len(first_half))
    second_sorted = merge_sort(second_half, len(second_half))
    merge_halfs = merge(first_sorted, second_sorted, arraylen)

    return merge_halfs


def merge(array1, array2, sumlen):
    result = []

    for _ in range(sumlen):
        if not array1 or not array2:
            result.extend(array1)
            result.extend(array2)
            break
        if array1[0] < array2[0]:
            result.append(array1.pop(0))
        else:
            result.append(array2.pop(0))

    return result
