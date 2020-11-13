from sys import stdin


def partition(values):
    truth_value = 0
    values = list(values)
    total = sum(values)
    if len(values) < 3 or total % 3:
        return truth_value
    third = total // 3
    table = [[0 for _ in range(len(values) + 1)] for _ in range(third + 1)]

    for i in range(1, third + 1):
        for j in range(1, len(values) + 1):
            ii = i - values[j - 1]
            if values[j - 1] == i or (ii > 0 and table[ii][j - 1]):
                if table[i][j - 1] == 0:
                    table[i][j] = 1
                else:
                    table[i][j] = 2
            else:
                table[i][j] = table[i][j - 1]
    if table[-1][-1] == 2:
        truth_value = 1

    return truth_value


def main():
    input_n, *input_values = list(map(int, stdin.read().split()))
    print(input_n)
    print(partition(input_values))


if __name__ == '__main__':
    main()