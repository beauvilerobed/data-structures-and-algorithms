import unittest
from arithmetic_expression import find_maximum_value


class arithmeticExpression(unittest.TestCase):
    def test(self):
        for s, answer in (
            ("5", 5),
            ("2+3", 5),
            ("2-3", -1),
            ("5-8+7*4-8+9", 200),
            ("8-5*3", 9),
            ("9*9*9*9", 9 * 9 * 9 * 9),
            ("1-1", 0),
            ("7", 7),
            ("1+2+3+4+5+6+7+8+9", 45)
        ):  
            self.assertEqual(find_maximum_value(s), answer)


if __name__ == '__main__':
    unittest.main()