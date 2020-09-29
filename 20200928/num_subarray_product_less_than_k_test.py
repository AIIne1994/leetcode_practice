import unittest
from num_subarray_product_less_than_k import *

class EvaluateDivisionTest(unittest.TestCase):
    def test_array_with_length_four(self):
        nums = [10, 5, 2, 6]
        k = 100
        expected = 8
        self.assertEqual(numSubarrayProductLessThanK(nums, k), expected)

    def test_k_is_zero(self):
        nums = [1, 2, 3]
        k = 0
        expected = 0
        self.assertEqual(numSubarrayProductLessThanK(nums, k), expected)

    def test_array_is_all_one(self):
        nums = [1, 1, 1]
        k = 1
        expected = 0
        self.assertEqual(numSubarrayProductLessThanK(nums, k), expected)


if __name__ == "__main__":
    unittest.main()
    