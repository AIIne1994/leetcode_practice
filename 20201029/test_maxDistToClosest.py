import unittest
from maxDistToClosest import *


class MaxDistToClosestTest(unittest.TestCase):
    def test_example_one(self):
        seats = [1,0,0,0,1,0,1]
        expected = 2
        self.assertEqual(maxDistToClosest(seats), expected)

    def test_example_two(self):
        seats = [1,0,0,0]
        expected = 3
        self.assertEqual(maxDistToClosest(seats), expected)

    def test_example_three(self):
        seats = [0,1]
        expected = 1
        self.assertEqual(maxDistToClosest(seats), expected)

    def test_example_four(self):
        seats = [0, 0, 1]
        expected = 2
        self.assertEqual(maxDistToClosest(seats), expected)

    def test_example_five(self):
        seats = [1, 0, 0, 1]
        expected = 1
        self.assertEqual(maxDistToClosest(seats), expected)

    def test_example_six(self):
        seats = [0, 1, 0, 0, 0, 0]
        expected = 4
        self.assertEqual(maxDistToClosest(seats), expected)


if __name__ == "__main__":
    unittest.main()
