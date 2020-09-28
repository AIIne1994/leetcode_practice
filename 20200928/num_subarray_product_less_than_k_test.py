import unittest
from num_subarray_product_less_than_k import *

class EvaluateDivisionTest(unittest.TestCase):
    def test_array_with_length_four(self):
        nums = [10, 5, 2, 6]
        k = 100
        expected = 8
        self.assertEqual(numSubarrayProductLessThanK(nums, k), expected)


if __name__ == "__main__":
    unittest.main()
    