import unittest
from random import randint
from max_salary import largest_number, largest_number_naive
from itertools import permutations


class TestLargestNumber(unittest.TestCase):
    def test_small(self):
        for numbers in [
            [1],
            [1, 2],
            [3, 4, 6, 9],
            [1, 12],
            [2, 12],
            [2, 21],
            [2, 21, 23, 211, 213, 231, 232]
        ]:
            self.assertEqual(largest_number(numbers),
                             largest_number_naive(numbers))

    def test_random(self):
        for n in range(2, 7):
            for max_value in [10, 20, 100, 1000]:
                for _ in range(10):
                    numbers = [randint(1, max_value) for _ in range(n)]
                    self.assertEqual(largest_number(numbers),
                                     largest_number_naive(numbers))


if __name__ == '__main__':
    unittest.main()
