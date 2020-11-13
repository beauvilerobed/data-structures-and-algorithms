import unittest
import math
from gcd import gcd, gcd_naive
    

class TestGCD(unittest.TestCase):
    def test_small(self):
        for (a, b) in [(1, 1), (2, 6), (12, 6)]:
            self.assertEqual(gcd(a, b), gcd_naive(a, b))
    
    def test_large(self):
        for (a, b, d) in [(28851538, 1183019, 17657), (222232244, 29420, 4)]:
            self.assertEqual(gcd(a, b), d)
    
    def test_more(self):
        for (a, b) in [(2, 3), (10**8, 10**5 - 1), (10**8, 10**9)]:
            self.assertEqual(gcd(a, b), math.gcd(a, b))


if __name__ == '__main__':
    unittest.main()