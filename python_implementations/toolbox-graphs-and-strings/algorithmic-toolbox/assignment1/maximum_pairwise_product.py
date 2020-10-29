

def max_pairwise_product_naive(numbers):
    product = 0

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            product = max(product, numbers[i] * numbers[j])

    return product


def max_pairwise_product(numbers):
    max_index1 = -1
    max_index2 = -1
    for i in range(len(numbers)):
        if (max_index1 == -1) | (numbers[i] > numbers[max_index1]):
            max_index1 = i
    
    for k in range(len(numbers)):
        if (k != max_index1) & ((max_index2 == -1) | (numbers[k] > numbers[max_index2])):
            max_index2 = k
    
    return numbers[max_index1] * numbers[max_index2]


def main():
    n = int(input())
    input_numbers = list(map(int, input().split()))
    assert len(input_numbers) == n
    print(max_pairwise_product(input_numbers))


if __name__ == '__main__':
    main()