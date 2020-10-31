from file_reader import read_multiple_files
import unittest
from trie import build_trie


files = read_multiple_files()

cases = list()
solutions = list()
for name in files:
    if name[-2:] == '.a':
        with open(name, 'r') as f:
            lines = f.readlines()
            lines = list(map(lambda x: x.rstrip('\n'), lines))
            solutions.append(lines)
    else:
        with open(name, 'r') as f:
            patterns = f.readlines()[1:]
            patterns = list(map(lambda x: x.rstrip('\n'), patterns))
            cases.append(patterns)


class BuildTrie(unittest.TestCase):
    def test(self):
        for pattern, solution in zip(cases, solutions):
            tree = build_trie(pattern)
            result = []
            for node in tree:
                for c in tree[node]:
                    result.append(str(node) + "->" + str(tree[node][c]) + ":" + str(c))
            result.sort()
            solution.sort()
            self.assertEqual(result, solution)


if __name__ == '__main__':
    unittest.main()