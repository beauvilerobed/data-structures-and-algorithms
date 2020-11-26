# python3

# KMP (Knuth Morris Pratt) Pattern Searching

# Find All Occurrences of a Pattern in a String

# Task. Find all occurrences of a pattern in a string.

import sys


def compute_prefix_function(prefix):
    n = len(prefix)
    s_function = [0 for _ in range(n)]
    s_function[0] = 0
    border = 0

    for i in range(1, n):
        while border > 0 and prefix[i] != prefix[border]:
            border = s_function[border-1]
        if prefix[i] == prefix[border]:
            border = border + 1
        else:
            border = 0
        s_function[i] = border
    return s_function


def find_pattern(pattern, text):
    """
    Find all the occurrences of the pattern in the text
    and return a list of all positions in the text
    where the pattern starts in the text.
    """
    p = len(pattern)
    pattern_text = pattern + '$' + text
    pattern_text_len = len(pattern_text)
    s = compute_prefix_function(pattern_text)
    result = []
    for i in range(p + 1, pattern_text_len):
        if s[i] == p:
            result.append(i - 2 * p)

    return result


def main():
    pattern = sys.stdin.readline().strip()
    text = sys.stdin.readline().strip()
    result = find_pattern(pattern, text)
    print(" ".join(map(str, result)))


if __name__ == '__main__':
    main()
