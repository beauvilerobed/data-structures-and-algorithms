# python3
import sys

# Multiple Pattern Matching Problem

# Find all occurrences of a collection of patterns in a text.

# Input: A string Text and a collection Patterns containing 
# (shorter) strings.

# Output: All starting positions in Text where a string from 
# Patterns appears as a substring.


def build_trie(patterns):
    tree = dict()
    tree[0] = {}
    count = 1
    for pattern in patterns:
        current_node = tree[0]
        for i in range(len(pattern)):
            current_symbol = pattern[i]
            if current_symbol in current_node:
                current_node = tree[current_node[current_symbol]]
            else:
                tree[count] = {}
                current_node[current_symbol] = count
                current_node = tree[count]
                count += 1
                
    return tree


def solve(text, n, patterns):
	result = []
	trie = build_trie(patterns)
	text_len = len(text)
	for i in range(text_len):
		if pattern_matches(text[i:], trie):
			result.append(i)
			
	return result

def pattern_matches(text, trie):
	current_symbol = text[0]
	current_node = trie[0]
	index = 0

	while True:
		if not current_node:
			return True
		elif current_symbol in current_node.keys():
			current_node = trie[current_node[current_symbol]]
			index += 1
			if index < len(text):
				current_symbol = text[index]
			else:
				current_symbol = '$'
		else:
			return False


def main():
	text = sys.stdin.readline().strip()
	n = int (sys.stdin.readline().strip())
	patterns = []
	for _ in range (n):
		patterns += [sys.stdin.readline().strip()]

	ans = solve (text, n, patterns)

	sys.stdout.write (' '.join (map (str, ans)) + '\n')


if __name__ == '__main__':
	main()