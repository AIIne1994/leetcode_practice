import unittest
from get_decimal_value import *


class GetDecimalValueTest(unittest.TestCase):
    def test_example_one(self):
        head = [1,0,1]
        expected = 5
        self.assertEqual(get_decimal_value(head), expected)

    def test_example_two(self):
        head = [0]
        expected = 0
        self.assertEqual(get_decimal_value(head), expected)

    def test_example_three(self):
        head = [1]
        expected = 1
        self.assertEqual(get_decimal_value(head), expected)

    def test_example_four(self):
        head = [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]
        expected = 18880
        self.assertEqual(get_decimal_value(head), expected)

    def test_example_four(self):
        head = [0,0]
        expected = 0
        self.assertEqual(get_decimal_value(head), expected)


if __name__ == "__main__":
    unittest.main()
    