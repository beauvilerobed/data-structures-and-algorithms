import unittest
from quicksort import quicksort

class TestQuicksort(unittest.TestCase):
  def test_base_case(self):
    expected = [1]
    actual = quicksort([1], 1)
    self.assertEqual(expected, actual)

  def test_array_len_2(self):
      expected = [1, 2]
      actual = quicksort([2, 1], 2)
      self.assertEqual(expected, actual)

  def test_array_len_3(self):
      expected = [1, 2, 3]
      actual = quicksort([2, 1, 3], 3)
      self.assertEqual(expected, actual)

  def test_array_len_even(self):
      expected = [1, 2, 3, 4, 5, 6]
      actual = quicksort([2, 5, 3, 6, 1, 4], 6)
      self.assertEqual(expected, actual)

  def test_array_len_odd(self):
      expected = [45, 49, 26, 22, 87, 65, 72, 41, 25]
      expected.sort()
      actual = quicksort([45, 49, 26, 22, 87, 65, 72, 41, 25], 9)
      self.assertEqual(expected, actual)
    
  def test_array_help_find_issue(self):
      expected = [45, 49, 26, 22, 87, 65, 72, 41, 25, 1, 59, 51, 69, 3, 47, 16, 93, 96, 32, 92, 83, 43, 86, 60, 75, 89, 39, 74, 81, 50, 77, 42, 97, 6, 62, 63, 36, 29, 52, 5, 14, 33, 55, 27, 57, 2, 82, 48, 40, 95, 7, 100, 15]
      expected.sort()
      actual = quicksort([45, 49, 26, 22, 87, 65, 72, 41, 25, 1, 59, 51, 69, 3, 47, 16, 93, 96, 32, 92, 83, 43, 86, 60, 75, 89, 39, 74, 81, 50, 77, 42, 97, 6, 62, 63, 36, 29, 52, 5, 14, 33, 55, 27, 57, 2, 82, 48, 40, 95, 7, 100, 15], 9)
      self.assertEqual(expected, actual)

if __name__ == '__main__':
  unittest.main()