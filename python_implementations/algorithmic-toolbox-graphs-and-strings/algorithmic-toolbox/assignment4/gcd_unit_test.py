import unittest
from gcd import gcd


def reference(a, b):
    for divisor in range(min(a,b), 0, -1):
        if a % divisor == 0 and b % divisor == 0:
            return divisor

class TestGCD(unittest.TestCase):
    def test_small(self):
        for (a, b) in [(1, 1), (2, 6), (12, 6)]:
            self.assertEqual(gcd(a, b), reference(a, b))
    
    def test_large(self):
        for (a, b, d) in [(28851538, 1183019, 17657), (222232244, 29420, 4)]:
            self.assertEqual(gcd(a, b), d)
    

if __name__ == '__main__':
    unittest.main()