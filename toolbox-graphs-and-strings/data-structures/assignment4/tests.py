import unittest
from job_queue import assign_jobs, assign_jobs_naive
import random
from file_reader import generate_files, generate_test_cases


files = generate_files()
solutions, test_cases = generate_test_cases(files)

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