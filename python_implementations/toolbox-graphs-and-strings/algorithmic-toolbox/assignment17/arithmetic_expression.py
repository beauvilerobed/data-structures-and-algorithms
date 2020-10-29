

import operator


def find_maximum_value(data_set):
    ops = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
    }

    operator_signs = []
    nums = []
    for val in data_set:
        if val in ops:
            operator_signs.append(ops[val])
        else:
            nums.append(int(val))
    nums_matrix1 = [[0 for _ in range(len(nums))] for _ in range(len(nums))]
    nums_matrix2 = [[0 for _ in range(len(nums))] for _ in range(len(nums))]
    for i in range(len(nums)):
        nums_matrix1[i][i] = nums[i]
        nums_matrix2[i][i] = nums[i]
    
    for s in range(1, len(nums)):
        for i in range(len(nums) - s):
            j = i + s
            nums_matrix1[i][j], nums_matrix2[i][j] = min_max(nums_matrix1, nums_matrix2, operator_signs, i, j)


    return nums_matrix2[0][len(nums) - 1]


def min_max(nums1, nums2, operator_signs, i, j):
    minimum = float("inf")
    maximum = -float("inf")
    for k in range(i, j):
        a = operator_signs[k](nums1[i][k], nums1[k + 1][j])
        b = operator_signs[k](nums1[i][k], nums2[k + 1][j])
        c = operator_signs[k](nums2[i][k], nums1[k + 1][j])
        d = operator_signs[k](nums2[i][k], nums2[k + 1][j])
        minimum = min(minimum, a, b, c, d)
        maximum = max(maximum, a, b, c, d)
    
    return minimum, maximum


def main():
    print(find_maximum_value(input()))


if __name__ == "__main__":
    main()