import sys

def two_sums(nums, targets):
    hash_it = set(nums)
    count = 0
    for target in targets:
        for num in nums:
            temp = target - num
            if temp != num and temp in hash_it:
                count += 1
                break
        
    return count

def find_two_sum_total(case, targets, n=1000):
    count = 0
    partition = int(10000/n)
    for i in range(-n, n):
        count += two_sums(case, targets[i * partition: (i+1) * partition])
        print("finished:", i * partition)
    
    count += two_sums(case, [targets[10000]])
    return count

def main():
    data = sys.stdin.read()
    data_set = list(map(int, data.split()))
    values = [-2, 3, 8, 11]
    is_sum = two_sums(data_set, values)
    print(is_sum)

if __name__ == '__main__':
    main()

