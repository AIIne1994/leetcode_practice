import unittest
from first_missing_possitive import *

class FirstMissingPossitiveTest(unittest.TestCase):
    def test_length_three(self):
        nums = [1, 2, 0]
        expected = 3
        self.assertEqual(firstMissingPositive(nums), expected)

    def test_length_four(self):
        nums = [3, 4, -1, 1]
        expected = 2
        self.assertEqual(firstMissingPositive(nums), expected)

    def test_length_five(self):
        nums = [7, 8, 9, 11, 12]
        expected = 1
        self.assertEqual(firstMissingPositive(nums), expected)


if __name__ == "__main__":
    unittest.main()
    