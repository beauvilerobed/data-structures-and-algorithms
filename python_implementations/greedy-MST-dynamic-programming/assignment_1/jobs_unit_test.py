import os
from jobs import scheduling, scheduling_ratio
import unittest

path = os.getcwd() + '/assignment.txt'

case = []
with open(path, 'r') as f:
    lines = f.readlines()
    for line in lines[1:]:
        weight, length = list(map(int, line.split()))
        case.append([weight, length])

# print(scheduling(case))
# print(scheduling_ratio(case))

class TestJobs(unittest.TestCase):
    def test_jobs_difference(self):
        actual = 74649
        expected = scheduling(case)
        self.assertEqual(actual, expected)
    
    def test_jobs_ratio(self):
        actual = 72468
        expected = scheduling_ratio(case)
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()