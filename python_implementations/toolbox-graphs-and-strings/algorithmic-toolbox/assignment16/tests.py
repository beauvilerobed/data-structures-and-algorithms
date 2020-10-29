import unittest
from partition_souvenirs import partition


class Partition(unittest.TestCase):
    def test(self):
        for values, answer in (
            ((20, ), 0),
            ((7, 7, 7), 1),
            ((3, 3, 3), 1),
            ((3, 3, 3, 3), 0),
            ((3, 6, 4, 1, 9, 6, 9, 1), 1),
            ((4, 1, 3, 2), 0)
        ):
            self.assertEqual(partition(values), answer)


if __name__ == '__main__':
    unittest.main()