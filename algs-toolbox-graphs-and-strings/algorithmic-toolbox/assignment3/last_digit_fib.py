# python3


def last_digit_of_fib_naive(n):
    if n <= 1:
        return n

    return (last_digit_of_fib_naive(n - 1) +
            last_digit_of_fib_naive(n - 2)) % 10


def last_digit_of_fib(n):
    prev = 0
    curr = 1

    # base case is taken care of here
    for _ in range(n):
        prev, curr = curr, (prev + curr) % 10

    return prev


def main():
    input_n = int(input())
    print(last_digit_of_fib(input_n))


if __name__ == '__main__':
    main()
