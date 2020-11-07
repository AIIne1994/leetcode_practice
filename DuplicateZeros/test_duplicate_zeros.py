import unittest
from duplicateZeros import *


class DuplicateZerosTest(unittest.TestCase):
    def test_example_one(self):
        arr = [1, 0, 2, 3, 0, 4, 5, 0]
        expected = [1, 0, 0, 2, 3, 0, 0, 4]
        duplicate_zeros(arr)
        self.assertEqual(arr, expected)

    def test_example_two(self):
        arr = [1, 0, 3, 0, 4, 5, 0]
        expected = [1,0,0,2,3,0,0,4]
        duplicate_zeros(arr)
        self.assertEqual(arr, expected)


if __name__ == "__main__":
    unittest.main()
