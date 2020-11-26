# python3


def max_pairwise_product_naive(numbers):
    product = 0

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            product = max(product, numbers[i] * numbers[j])

    return product


def max_pairwise_product(numbers):
    first = -float("inf")
    second = -float("inf")
    first_index = int()
    second_index = int()

    # find the first largest value
    for i in range(len(numbers)):
        if numbers[i] > first:
            first = numbers[i]
            first_index = i

    # find the second largest value different from the first
    for j in range(len(numbers)):
        if numbers[j] > second and j != first_index:
            second = numbers[j]
            second_index = j

    return numbers[first_index] * numbers[second_index]


def main():
    n = int(input())
    input_numbers = list(map(int, input().split()))
    assert len(input_numbers) == n
    print(max_pairwise_product(input_numbers))


if __name__ == '__main__':
    main()
