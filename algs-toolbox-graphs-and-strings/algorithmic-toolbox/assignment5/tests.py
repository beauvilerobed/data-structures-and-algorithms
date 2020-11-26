import unittest
from itertools import product
from fib_number_again import fib_number_again, fib_number_again_naive


class TestFibNumberAgain(unittest.TestCase):
    def test_small(self):
        for n, m in product(range(2, 15), repeat=2):
            self.assertEqual(fib_number_again(n, m),
                             fib_number_again_naive(n, m))

    def test_large(self):
        for (n, m, r) in [(115, 1000, 885),
                          (2816213588, 239, 151),
                          (300, 17, 8)]:
            self.assertEqual(fib_number_again(n, m), r)


if __name__ == '__main__':
    unittest.main()
