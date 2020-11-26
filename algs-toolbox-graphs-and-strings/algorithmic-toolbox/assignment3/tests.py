import unittest
from last_digit_fib import last_digit_of_fib, last_digit_of_fib_naive


class TestLastDigitFib(unittest.TestCase):
    def test_small(self):
        for n in range(20):
            self.assertEqual(last_digit_of_fib(n), last_digit_of_fib_naive(n))

    def test_large(self):
        for (n, last_digit) in [(1000, 5), (139, 1), (91239, 6), (999999, 6)]:
            self.assertEqual(last_digit_of_fib(n), last_digit)


if __name__ == '__main__':
    unittest.main()
