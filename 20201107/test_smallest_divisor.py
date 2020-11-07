import unittest
from smallest_divisor import *


class SmallestDivisorTest(unittest.TestCase):
    def test_example_one(self):
        nums = [1,2,5,9]
        threshold = 6
        expected = 5
        self.assertEqual(smallest_divisor(nums, threshold), expected)

    def test_example_two(self):
        nums = [2,3,5,7,11]
        threshold = 11
        expected = 3
        self.assertEqual(smallest_divisor(nums, threshold), expected)

    def test_example_one(self):
        nums = [19]
        threshold = 5
        expected = 4
        self.assertEqual(smallest_divisor(nums, threshold), expected)


if __name__ == "__main__":
    unittest.main()
    