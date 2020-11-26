def fib_number_again_naive(n, m):
    if n <= 1:
        return n

    previous, current = 0, 1
    for _ in range(n):
        previous, current = current, (previous + current) % m

    return previous


def fib_number_again(n, m):
    # return pisano period here
    n = n % return_period(m)
    previous, current = 0, 1

    for _ in range(n):
        previous, current = current, (previous + current) % m

    return previous


def return_period(m):
    previous, current = 0, 1
    # procedure to find pisano period
    for i in range(m * m):
        previous, current = current, (previous + current) % m
        if (previous == 0) & (current == 1):
            return i + 1


def main():
    input_n, input_m = map(int, input().split())
    print(fib_number_again(input_n, input_m))


if __name__ == '__main__':
    main()
