from itertools import permutations


def largest_number_naive(numbers):
    numbers = list(map(str, numbers))

    largest = 0

    for permutation in permutations(numbers):
        largest = max(largest, int("".join(permutation)))

    return largest


def largest_number(numbers):
    numbers = list(map(str, numbers))
    for _ in range(len(numbers) - 1):
        for i in range(len(numbers) - 1):
            if numbers[i] + numbers[i + 1] < numbers[i + 1] + numbers[i]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]

    return int("".join(numbers))


if __name__ == '__main__':
    n = int(input())
    input_numbers = input().split()
    print(largest_number(input_numbers))