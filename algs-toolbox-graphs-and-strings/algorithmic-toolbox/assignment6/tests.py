import unittest
from money_change import money_change


def reference(money):
    return (money // 10) + ((money % 10) // 5) + (money % 5)


class TestSumOfTwoDigits(unittest.TestCase):
    def test(self):
        for (money, number_of_coins) in [(1, 1), (2, 2), (28, 6)]:
            self.assertEqual(money_change(money), number_of_coins)

    def test_more(self):
        for m in range(10 ** 3):
            self.assertEqual(money_change(m), reference(m))


if __name__ == '__main__':
    unittest.main()
