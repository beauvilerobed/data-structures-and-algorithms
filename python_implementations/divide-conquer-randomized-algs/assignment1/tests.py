import unittest
from karatsuba import karatsuba
from file_reader import generate_paths, generate_tests

paths = generate_paths()
cases = generate_tests(paths)

class TestKaratsuba(unittest.TestCase):
  def test_cases(self):
    for case in cases:
      first = case[0]
      second = case[1]
      self.assertEqual(karatsuba(first, second), first * second)
    
if __name__ == '__main__':
  unittest.main()