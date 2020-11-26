# python3

# Construct the Suffix Array of a Long String

# Task. Construct the suffix array of a string.

import sys


def sort_character(text):
    n = len(text)
    m = 256
    order = [0 for _ in range(n)]
    count = [0 for _ in range(m)]

    for i in range(n):
        count[ord(text[i])] = count[ord(text[i])] + 1
    for j in range(1, m):
        count[j] = count[j] + count[j - 1]
    for k in range(n):
        char = ord(text[n - k - 1])
        count[char] = count[char] - 1
        order[count[char]] = n - k - 1
    return order


def computer_char_classes(text, order):
    n = len(text)
    classes = [0 for _ in range(n)]
    classes[order[0]] = 0
    for i in range(1, n):
        if text[order[i]] != text[order[i-1]]:
            classes[order[i]] = classes[order[i-1]] + 1
        else:
            classes[order[i]] = classes[order[i-1]]
    return classes


def sort_doubled(text, l, order, classes):
    n = len(text)
    count = [0 for _ in range(n)]
    new_order = [0 for _ in range(n)]
    for i in range(n):
        count[classes[i]] = count[classes[i]] + 1
    for j in range(1, n):
        count[j] = count[j] + count[j-1]
    for k in range(n):
        start = (order[n - k - 1] - l + n) % n
        cl = classes[start]
        count[cl] = count[cl] - 1
        new_order[count[cl]] = start
    return new_order


def update_classes(new_order, classes, l):
    m = len(new_order)
    new_classes = [0 for _ in range(m)]
    new_classes[new_order[0]] = 0
    for i in range(1, m):
        curr = new_order[i]
        prev = new_order[i-1]
        mid = (curr + l) % m
        mid_prev = (prev + l) % m
        if classes[curr] != classes[prev] or classes[mid] != classes[mid_prev]:
            new_classes[curr] = new_classes[prev] + 1
        else:
            new_classes[curr] = new_classes[prev]

    return new_classes


def build_suffix_array(text):
    """
    Build suffix array of the string text and
    return a list result of the same length as the text
    such that the value result[i] is the index (0-based)
    in text where the i-th lexicographically smallest
    suffix of text starts.
    """
    order = sort_character(text)
    classes = computer_char_classes(text, order)
    l = 1
    while l < len(text):
        order = sort_doubled(text, l, order, classes)
        classes = update_classes(order, classes, l)
        l = 2 * l
    return order


def main():
    text = sys.stdin.readline().strip()
    print(" ".join(map(str, build_suffix_array(text))))


if __name__ == '__main__':
    main()
