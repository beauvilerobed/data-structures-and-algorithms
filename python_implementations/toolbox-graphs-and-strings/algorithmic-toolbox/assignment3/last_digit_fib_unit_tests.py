import unittest
from last_digit_fib import last_digit_of_fib

def reference(n):
    if n <= 1:
        return n
    
    return (reference(n - 1) + reference(n - 2)) % 10


class TestLastDigitFib(unittest.TestCase):
    def test_small(self):
        for n in range(20):
            self.assertEqual(last_digit_of_fib(n), reference(n))
    
    def test_large(self):
        for (n, last_digit) in [(1000, 5), (139, 1), (91239, 6), (999999, 6)]:
            self.assertEqual(last_digit_of_fib(n), last_digit)

if __name__ == '__main__':
    unittest.main()