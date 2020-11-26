def lcs2(first_sequence, second_sequence):
    nn, mm = len(first_sequence), len(second_sequence)
    matrix = [[0 for _ in range(mm + 1)] for _ in range(nn + 1)]

    for i in range(1, nn + 1):
        for j in range(1, mm + 1):
            if first_sequence[i - 1] == second_sequence[j - 1]:
                matrix[i][j] = max(matrix[i - 1][j - 1] + 1,
                                   matrix[i][j - 1], matrix[i - 1][j])
            else:
                matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1])

    return matrix[nn][mm]


def main():
    n = int(input())
    a = list(map(int, input().split()))

    m = int(input())
    b = list(map(int, input().split()))
    print(m, n)
    print(lcs2(a, b))

if __name__ == '__main__':
    main()
