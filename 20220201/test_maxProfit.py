import unittest
from maxProfit import *

class MaxProfitTest(unittest.TestCase):
    def test_example_one(self):
        prices = [7, 1, 5, 3, 6, 4]
        expected = 5
        result = maxProfit(prices)
        self.assertEqual(result, expected)

    def test_example_two(self):
        prices = [7, 6, 4, 3, 1]
        expected = 0
        result = maxProfit(prices)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
    