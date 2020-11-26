# python3


def majority_element_naive(elements):
    for element in elements:
        if elements.count(element) > len(elements) / 2:
            return 1

    return 0


def majority_element(elements):
    hash_it = {}
    for element in elements:
        if element in hash_it:
            hash_it[element] += 1
        else:
            hash_it[element] = 1

    for key in hash_it:
        if hash_it[key] > len(elements) / 2:
            return 1

    return 0


def main():
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    print('number of elements:', input_n)
    print(majority_element(input_elements))


if __name__ == '__main__':
    main()
