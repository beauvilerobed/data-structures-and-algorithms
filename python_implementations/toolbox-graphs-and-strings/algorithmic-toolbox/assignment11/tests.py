import unittest
from majority_element import majority_element

def reference(elements):
    for element in elements:
        if elements.count(element) > len(elements) / 2:
            return 1
    
    return 0

class TestMajorityElement(unittest.TestCase):
    def test_small(self):
        for elements in [
            [7, 2, 7],
            [7, 8, 9],
            [2, 3, 2, 3],
            [1, 2, 3, 4],
            [1, 2, 2]
        ]:
            self.assertEqual(
                majority_element(list(elements)),
                reference(elements)
            )
    
    def test_large(self):
        for (elements, answer) in [
            ([0] * 5000 + [1] * 5000, 0)
        ]:  
            self.assertEqual(majority_element(elements), answer)

if __name__ == '__main__':
    unittest.main()