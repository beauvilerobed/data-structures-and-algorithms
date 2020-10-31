# python3
import sys

# Reconstruct a String from its Burrows–Wheeler Transform

# Task. Reconstruct a string from its Burrows–Wheeler transform

def InverseBWT(bwt):
    n = len(bwt)
    bwt_set = {}
    bwt_array = []

    for letter in bwt:
        if letter in bwt_set:
            bwt_set[letter] += 1
        else:
            bwt_set[letter] = 1
        bwt_array.append((letter, bwt_set[letter]))
    
    sorted_bwt_array = sorted(bwt_array)
    enum_sorted_bwt_array = {}
    for i in range(n):
        key = sorted_bwt_array[i]
        enum_sorted_bwt_array[key] = i
    
    result = ''
    index = 0
    while len(result) < n - 1:
        result += bwt_array[index][0]
        letter_and_number = (bwt_array[index][0], bwt_array[index][1])
        index = enum_sorted_bwt_array[letter_and_number]


    return result[::-1] + '$'


def main():
    bwt = sys.stdin.readline().strip()
    print(InverseBWT(bwt))


if __name__ == '__main__':
    main()