import unittest
from fibonacci import fibonacci_number

def reference(n):
    if n <= 1:
        return n
    
    return reference(n - 1) + reference(n - 2) 

class TestFibonacciNumber(unittest.TestCase):
    def test_small(self):
        for n in range(8):
            self.assertEqual(fibonacci_number(n), reference(n))
        
    def test_large(self):
        for (n, Fn) in [(30, 832040), (35, 9227465), (40, 102334155)]:
            self.assertEqual(fibonacci_number(n), Fn)

if __name__ == '__main__':
    unittest.main()