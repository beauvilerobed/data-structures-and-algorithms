import sys


def two_sums(nums, target):
    hash_it = set(nums)
    count = 0
    for num in nums:
        temp = target - num
        if temp != num and temp in hash_it:
            count += 1
            break

    return count


def find_two_sum_total(case, targets):
    count = 0
    for i in range(len(targets)):
        count += two_sums(case, targets[i])

    return count


def main():
    data = sys.stdin.read()
    data_set = list(map(int, data.split()))
    values = [-2, 3, 8, 11]
    is_sum = two_sums(data_set, values)
    print(is_sum)


if __name__ == '__main__':
    main()
