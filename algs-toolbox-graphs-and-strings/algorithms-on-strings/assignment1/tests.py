from file_reader import read_multiple_files, return_cases
import unittest
from trie import build_trie


class BuildTrie(unittest.TestCase):
    def test(self):
        files = read_multiple_files()
        cases, solutions = return_cases(files)

        assert len(files) > 0
        assert len(cases) > 0
        assert len(solutions) > 0
        
        for pattern, solution in zip(cases, solutions):
            tree = build_trie(pattern)
            result = []
            for node in tree:
                for c in tree[node]:
                    result.append(str(node) + "->" +
                                  str(tree[node][c]) + ":" + str(c))
            result.sort()
            solution.sort()
            self.assertEqual(result, solution)


if __name__ == '__main__':
    unittest.main()
