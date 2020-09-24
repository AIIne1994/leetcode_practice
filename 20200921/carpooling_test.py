import unittest
from carpooling import *

class CarpoolingTest(unittest.TestCase):
    def test_two_trips_with_capacity_with_four(self):
        trips = [[2, 1, 5], [3, 3, 7]]
        capacity = 4
        expected = False
        self.assertEqual(carPooling(trips, capacity), expected)

    def test_two_trips_with_capacity_with_five(self):
        trips = [[2, 1, 5], [3, 3, 7]]
        capacity = 5
        expected = True
        self.assertEqual(carPooling(trips, capacity), expected)

    def test_another_two_trips_with_capacity_with_four(self):
        trips = [[2, 1, 5], [3, 5, 7]]
        capacity = 3
        expected = True
        self.assertEqual(carPooling(trips, capacity), expected)

    def test_three_trips_with_capacity_with_four(self):
        trips = [[3, 2 ,7], [3 , 7, 9], [8, 3, 9]]
        capacity = 11
        expected = True
        self.assertEqual(carPooling(trips, capacity), expected)

if __name__ == "__main__":
    unittest.main()
    