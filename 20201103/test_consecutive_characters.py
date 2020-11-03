import unittest
from consecutive_characters import *

class MaxPowerTest(unittest.TestCase):
    def test_example_one(self):
        s = "leetcode"
        expected = 2
        self.assertEqual(max_power(s), expected)

    def test_example_two(self):
        s = "abbcccddddeeeeedcba"
        expected = 5
        self.assertEqual(max_power(s), expected)

    def test_example_three(self):
        s = "triplepillooooow"
        expected = 5
        self.assertEqual(max_power(s), expected)

    def test_example_four(self):
        s = "hooraaaaaaaaaaay"
        expected = 11
        self.assertEqual(max_power(s), expected)

    def test_example_five(self):
        s = "tourist"
        expected = 1
        self.assertEqual(max_power(s), expected)

    def test_example_six(self):
        s = "cc"
        expected = 2
        self.assertEqual(max_power(s), expected)


if __name__ == "__main__":
    unittest.main()
