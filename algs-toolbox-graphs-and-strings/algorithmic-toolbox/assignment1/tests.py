import unittest
from random import randint
from maximum_pairwise_product import max_pairwise_product,\
                                     max_pairwise_product_naive


class TestMaxPairwiseProduct(unittest.TestCase):
    def test_small(self):
        self.assertEqual(max_pairwise_product([1, 2, 3]), 6)
        self.assertEqual(max_pairwise_product([9, 3, 2]), 27)
        self.assertEqual(max_pairwise_product([9, 3, 1, 9]), 81)

    def test_stress(self):
        number_of_iterations = 10
        array_size = 100
        max_number = 2 * 10 ** 5

        for _ in range(number_of_iterations):
            numbers = [randint(0, max_number) for _ in range(array_size)]
            self.assertEqual(max_pairwise_product(numbers),
                             max_pairwise_product_naive(numbers))

    def test_large(self):
        self.assertEqual(max_pairwise_product([4] * (2 * 10 ** 5)), 16)
        self.assertEqual(max_pairwise_product([x for x in range(10 ** 5)]),
                                             (10 ** 5 - 1) * (10 ** 5 - 2))
        self.assertEqual(max_pairwise_product([1] * (2 * 10 ** 5)), 1)

    def test_more(self):
        tests = [
            ([1, 2], 2),
            ([2, 1], 2),
            ([3, 5], 15),
            ([5, 3], 15),
            ([7, 7], 49),
            ([5, 1, 5], 25),
            ([1, 5, 5], 25),
            ([i + 1 for i in range(10**5)], (10**5 - 1) * (10 ** 5)),
        ]
        for array, answer in tests:
            self.assertEqual(max_pairwise_product(array), answer)


if __name__ == '__main__':
    unittest.main()
