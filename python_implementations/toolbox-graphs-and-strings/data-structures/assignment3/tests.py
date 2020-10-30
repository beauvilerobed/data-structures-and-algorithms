import unittest
from build_heap import build_heap
import glob
import os


path = os.getcwd() + "/tests/*"
files = glob.glob(path)
files.sort()
solution = []
cases = []

for name in files:
    with open(name, "r") as f:
        if name[-2:] == ".a":
            lines = f.readlines()
            solution = []
            for line in lines:
                solution.append(list(map(int, line.split())))
        else:
            lines = f.readlines()
            lines = lines[1:]
            test_case = []
            for line in lines:
                case = list(map(int, line.split()))
                test_case.extend(case)


class MakeHeap(unittest.TestCase):
    def test(self):
        self.assertEqual(solution[1:], build_heap(test_case))

if __name__ == '__main__':
    unittest.main()