

def fibonacci_number(n):
    if n <= 1:
        return n
    
    previous, current = 0, 1
    for _ in range(n):
        previous, current = current, (current + previous)

    return previous


def main():
    input_n = int(input())
    print(fibonacci_number(input_n))


if __name__ == '__main__':
    main()