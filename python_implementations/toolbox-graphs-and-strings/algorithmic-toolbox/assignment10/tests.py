import unittest
from binary_search import binary_search

def reference(keys, query):
    for i in range(len(keys)):
        if keys[i] == query:
            return i
    
    return -1

class TestBinarySearch(unittest.TestCase):
    def test_small(self):
        for (keys, query) in [
            ([1, 2, 3], 1),
            ([4, 5, 6], 7),
            ([1, 3, 7, 8, 9, 12, 15], 12)
        ]:
            self.assertEqual(
                reference(keys, query),
                binary_search(keys, query)
            )
    
    def test_large(self):
        for (keys, query, answer) in [
            (list(range(10 ** 4)), 10 ** 4, -1),
            (list(range(10 ** 4)), 10 **4 - 1, 10 ** 4 - 1),
            (list(range(10 ** 4)), 239, 239),
        ]:
            self.assertEqual(binary_search(keys, query), answer)


if __name__ == '__main__':
    unittest.main()