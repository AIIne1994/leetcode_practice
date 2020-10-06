import unittest
from insert_into_bst import *

null = None
class InsertIntoBSTTest(unittest.TestCase):
    def test_example_one(self):
        root = [4,2,7,1,3]
        val = 5
        expected = [4,2,7,1,3,5]
        self.assertEqual(bitwise_complement(num), expected)

    def test_example_two(self):
        root = [40,20,60,10,30,50,70]
        val = 25
        expected = [40,20,60,10,30,50,70,null,null,25]
        self.assertEqual(bitwise_complement(num), expected)

    def test_example_three(self):
        root = [4,2,7,1,3,null,null,null,null,null,null]
        val = 5
        expected = [4,2,7,1,3,5]
        self.assertEqual(bitwise_complement(num), expected)


if __name__ == "__main__":
    unittest.main()
