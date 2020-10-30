import unittest
from job_queue import assign_jobs, assign_jobs_naive
import glob
import os
import random

from collections import namedtuple

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])

path = os.getcwd() + "/tests/*"
files = glob.glob(path)
files.sort()

solutions = []
test_cases = []

for name in files:
    with open(name, "r") as f:
        if name[-2:] == ".a":
            lines = f.readlines()
            temp = []
            for line in lines:
                solution_list = list(map(int, line.split()))
                solution = AssignedJob(solution_list[0], solution_list[1])
                temp.append(solution)
            solutions.append(temp)
        else:
            lines = f.readlines()
            temp = []
            elements = list(map(int, lines[0].split()))
            temp.append(elements[0])
            for line in lines[1:]:
                partial = list(map(int, line.split()))
                temp.extend(partial)
            test_cases.append(temp)
             

class JobQueue(unittest.TestCase):
    def test(self):
        for solution, cases in zip(solutions, test_cases):
            n_workers = cases[0]
            jobs = cases[1:]
            self.assertEqual(solution, assign_jobs(n_workers, jobs))
    
    def test_stress(self):
        for _ in range(20):
            numbers = []
            for _ in range(10):
                numbers.append(random.randint(1, 20))
            self.assertEqual(assign_jobs(10, numbers), assign_jobs_naive(10, numbers))

if __name__ == '__main__':
    unittest.main()