import unittest
from karatsuba import karatsuba
import os
import glob

test_case_path = os.getcwd() + '/tests/*'
paths = glob.glob(test_case_path)

cases = []
for path in paths:
  with open(path, 'r') as f:
    lines = f.readlines()
    number_pair = list(map(int, lines))
    cases.append(number_pair)


class TestKaratsuba(unittest.TestCase):
  def test_cases(self):
    for case in cases:
      first = case[0]
      second = case[1]
      self.assertEqual(karatsuba(first, second), first * second)
    
if __name__ == '__main__':
  unittest.main()