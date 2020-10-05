import unittest
from compoment_of_base_ten_integer import *

class BitwiseComplementTest(unittest.TestCase):
    def test_example_one(self):
        num = 5
        expected = 2
        self.assertEqual(bitwise_complement(num), expected)

    def test_example_two(self):
        num = 7
        expected = 0
        self.assertEqual(bitwise_complement(num), expected)

    def test_example_three(self):
        num = 10
        expected = 5
        self.assertEqual(bitwise_complement(num), expected)


if __name__ == "__main__":
    unittest.main()
