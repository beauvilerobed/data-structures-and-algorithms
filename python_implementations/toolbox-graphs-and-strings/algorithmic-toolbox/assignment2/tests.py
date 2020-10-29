import unittest
from fibonacci import fibonacci_number, fibonacci_number_naive


class TestFibonacciNumber(unittest.TestCase):
    def test_small(self):
        for n in range(8):
            self.assertEqual(fibonacci_number(n), fibonacci_number_naive(n))
    
    def test_more(self):
        for x in range(41):
            self.assertEqual(fibonacci_number(x), fibonacci_number_naive(x))
            print("passed case", x)
        
    def test_large(self):
        for (n, Fn) in [(30, 832040), (35, 9227465), (40, 102334155)]:
            self.assertEqual(fibonacci_number(n), Fn)


if __name__ == '__main__':
    unittest.main()