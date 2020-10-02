import unittest
from number_of_recent_calls import *

class NumberOfRecentCallsTest(unittest.TestCase):
    def test_simple_one(self):
        candidates =[2, 3, 6, 6]
        target = 7
        expected = [[2, 2, 3], [7]]
        self.assertEqual(combination_sum(candidates, target), expected)

    def test_example_two(self):
        candidates =[2, 3, 5]
        target = 8
        expected = [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
        self.assertEqual(combination_sum(candidates, target), expected)

    def test_example_three(self):
        candidates = [2]
        target = 1
        expected = []
        self.assertEqual(combination_sum(candidates, target), expected)

    def test_example_four(self):
        candidates =[1]
        target = 1
        expected = [[1]]
        self.assertEqual(combination_sum(candidates, target), expected)

    def test_example_five(self):
        candidates = [1]
        target = 2
        expected = [[1, 1]]
        self.assertEqual(combination_sum(candidates, target), expected)


if __name__ == "__main__":
    unittest.main()
    