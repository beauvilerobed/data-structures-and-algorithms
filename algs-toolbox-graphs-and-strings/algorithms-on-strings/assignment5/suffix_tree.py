# python3

# Construct a Trie from a Collection of Patterns

# Task. Construct a trie from a collection of patterns.

import sys

sys.setrecursionlimit(10000)


class SuffixTree:
    class Node:
        def __init__(self, label):
            self.label = label
            self.out_edges = {}

    def __init__(self, text):
        """ Make suffix tree from text in quadratic
                time and linear space"""
        self.root_node = self.Node(None)
        self.root_node.out_edges[text[0]] = self.Node(text)
        # add the rest of the suffixes, from longest to shortest
        for i in range(1, len(text)):
            # start at root and then walk down as far as possible
            current_node = self.root_node
            j = i
            while j < len(text):
                if text[j] in current_node.out_edges:
                    child = current_node.out_edges[text[j]]
                    label = child.label

                    k = j + 1
                    while k - j < len(label) and text[k] == label[k-j]:
                        k += 1
                    if k - j == len(label):
                        current_node = child  # we gone as far as possible
                        j = k
                    else:
                        cExist, cNew = label[k-j], text[k]
                        mid = self.Node(label[:k-j])
                        mid.out_edges[cNew] = self.Node(text[k:])
                        mid.out_edges[cExist] = child
                        child.label = label[k-j:]
                        current_node.out_edges[text[j]] = mid
                else:
                    current_node.out_edges[text[j]] = self.Node(text[j:])

    def return_suffix_list(self, node, suffix_tree_list):
        for child in node.out_edges:
            suffix_tree_list.append(node.out_edges[child].label)
            self.return_suffix_list(node.out_edges[child], suffix_tree_list)

        return suffix_tree_list


def build_suffix_tree(text):
    """
    Build a suffix tree of the string text and return a list
    with all of the labels of its edges (the corresponding
    substrings of the text) in any order.
    """
    result = []
    suffix_tree = SuffixTree(text)
    result = suffix_tree.return_suffix_list(suffix_tree.root_node, result)
    return result


def main():
    text = sys.stdin.readline().strip()
    result = build_suffix_tree(text)
    print("\n".join(result))


if __name__ == '__main__':
    main()
