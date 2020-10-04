import unittest
from remove_covered_intervals import *

class RemoveCoverdIntervalsTest(unittest.TestCase):
    def test_example_one(self):
        intervals = [[1,4],[3,6],[2,8]]
        expected = 2
        self.assertEqual(remove_covered_intervals(intervals), expected)

    def test_example_two(self):
        intervals = [[1,4],[2,3]]
        expected = 1
        self.assertEqual(remove_covered_intervals(intervals), expected)

    def test_example_three(self):
        intervals = [[0,10],[5,12]]
        expected = 2
        self.assertEqual(remove_covered_intervals(intervals), expected)

    def test_example_four(self):
        intervals = [[3,10],[4,10],[5,11]]
        expected = 2
        self.assertEqual(remove_covered_intervals(intervals), expected)

    def test_example_five(self):
        intervals = [[1,2],[1,4],[3,4]]
        expected = 1
        self.assertEqual(remove_covered_intervals(intervals), expected)


if __name__ == "__main__":
    unittest.main()
