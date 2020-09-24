import unittest
from find_the_difference import *

class FindTheDifferenceTest(unittest.TestCase):
    def test_the_difference_at_the_end(self):
        s = "abcd"
        t = "abcde"
        expected = "e"
        self.assertEqual(findTheDifference(s, t), expected)


if __name__ == "__main__":
    unittest.main()
    