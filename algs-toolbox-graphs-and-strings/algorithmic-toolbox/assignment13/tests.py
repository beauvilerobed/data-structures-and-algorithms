import unittest
from money_change_again import change


def reference(money):
    min_coins = float("inf")

    for num1 in range(money + 1):
        for num3 in range(money // 3 + 1):
            for num4 in range(money // 4 + 1):
                if 1 * num1 + 3 * num3 + 4 * num4 == money:
                    min_coins = min(min_coins, num1 + num3 + num4)

    return min_coins


class MoneyChangeAgain(unittest.TestCase):
    def test_small(self):
        for money in range(1, 40):
            self.assertEqual(change(money), reference(money))

    def test_large(self):
        for money, answer in ((200, 50), (239, 60), (31, 8)):
            self.assertEqual(change(money), answer)


if __name__ == '__main__':
    unittest.main()
