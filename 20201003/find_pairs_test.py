import unittest
from find_pairs import *

class FindPairsTest(unittest.TestCase):
    def test_example_one(self):
        nums = [3, 1, 4, 1, 5]
        k = 2
        expected = 2
        self.assertEqual(find_pairs(nums, k), expected)

    def test_example_two(self):
        nums = [1, 2, 3, 4, 5]
        k = 1
        expected = 4
        self.assertEqual(find_pairs(nums, k), expected)

    def test_example_three(self):
        nums = [1, 3, 1, 5, 4]
        k = 0
        expected = 1
        self.assertEqual(find_pairs(nums, k), expected)

    def test_example_four(self):
        nums = [1, 2, 4, 4, 3, 3, 0, 9, 2, 3]
        k = 3
        expected = 2
        self.assertEqual(find_pairs(nums, k), expected)

    def test_example_five(self):
        nums = [-1, -2, -3]
        k = 1
        expected = 2
        self.assertEqual(find_pairs(nums, k), expected)

    def test_all_the_same(self):
        nums = [1, 1, 1, 1, 1]
        k = 0
        expected = 1
        self.assertEqual(find_pairs(nums, k), expected)


if __name__ == "__main__":
    unittest.main()
    