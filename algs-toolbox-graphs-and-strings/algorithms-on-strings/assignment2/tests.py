from file_reader import read_multiple_files
import unittest
from trie_matching import solve


files = read_multiple_files()

cases = list()
solutions = list()
for name in files:
    if name[-2:] == '.a':
        with open(name, 'r') as f:
            lines = list(map(int, f.readline().split()))
            solutions.append(lines)
    else:
        with open(name, 'r') as f:
            lines = f.readlines()
            text = lines[0].strip()
            n = int(lines[1].strip())
            patterns = list(map(lambda x: x.rstrip('\n'), lines[2:]))
            cases.append([text, n, patterns])


class Solve(unittest.TestCase):
    def test(self):
        for case, solution in zip(cases, solutions):
            text = case[0]
            n = case[1]
            patterns = case[2]
            self.assertEqual(solve(text, n, patterns), solution)


if __name__ == '__main__':
    unittest.main()
