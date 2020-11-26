def gcd_naive(a, b):
    for divisor in range(min(a, b), 0, -1):
        if a % divisor == 0 and b % divisor == 0:
            return divisor


def gcd(a, b):
    while b % a != 0:
        a, b = b, a % b

    return a


def reference(a, b):
    if b == 0:
        return a
    else:
        # gcd(a, b) = gcd(b, a % b) by euclid's algorithm
        return reference(b, a % b)


def main():
    input_a, input_b = map(int, input().split())
    print(gcd(input_a, input_b))


if __name__ == '__main__':
    main()
