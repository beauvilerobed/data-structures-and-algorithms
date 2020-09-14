import unittest
from karatsuba import karatsuba

class TestKaratsuba(unittest.TestCase):
  def test_positive_integers(self):
    expected = 123456789 * 987654321
    actual = karatsuba('123456789', '987654321')
    self.assertEqual(expected, actual)

  def test_assignment(self):
    expected = 3141592653589793238462643383279502884197169399375105820974944592 * 2718281828459045235360287471352662497757247093699959574966967627
    actual = karatsuba('3141592653589793238462643383279502884197169399375105820974944592', '2718281828459045235360287471352662497757247093699959574966967627')
    self.assertEqual(expected, actual)
    
if __name__ == '__main__':
  unittest.main()