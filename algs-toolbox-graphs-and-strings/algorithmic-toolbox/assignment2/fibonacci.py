def fibonacci_number_naive(n):
    if n <= 1:
        return n

    return fibonacci_number_naive(n - 1) + fibonacci_number_naive(n - 2)


def fibonacci_number(n):
    prev = 0
    curr = 1

    # base case is taken care of here
    for _ in range(n):
        prev, curr = curr, prev + curr

    return prev


def main():
    input_n = int(input())
    print(fibonacci_number(input_n))


if __name__ == '__main__':
    main()
