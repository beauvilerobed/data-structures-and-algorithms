import unittest
from check_brackets import find_mismatch
import glob
import errno
import os


path = os.getcwd() + "/tests/*"
files = glob.glob(path)
files.sort()

solutions = []
cases = []
for name in files:
    try:
        with open(name, "r") as f:
            if name[-2:] == ".a":
                line = f.readline()
                solutions.append(line.split()[0])
            else:
                lines = f.readlines()
                test_case = ''
                for line in lines:
                    test_case += line.split()[0]
                cases.append(test_case)
    except IOError as exc:
        if exc.errno != errno.EISDIR:
            raise


class CheckBrackets(unittest.TestCase):
    def test(self):
        for i in range(len(cases)):
            self.assertEqual(solutions[i], find_mismatch(cases[i]))


if __name__ == '__main__':
    unittest.main()