import unittest
from largestNumber import *

class LargestNumberTest(unittest.TestCase):
    def test_largest_number_with_list_length_is_two(self):
        nums = [10,2]
        expected = "210"
        self.assertEqual(largestNumber(nums), expected)

    def test_largest_number_with_list_length_is_five(self):
        nums = [3,30,34,5,9]
        expected = "9534330"
        self.assertEqual(largestNumber(nums), expected)


if __name__ == "__main__":
    unittest.main()
