import unittest
from number_of_recent_calls import *

class NumberOfRecentCallsTest(unittest.TestCase):
    def setUp(self):
        self.NRC = RecentCounter()

    def test_add_one_call(self):
        self.assertEqual(self.NRC.ping(1), 1)

    def test_add_two_call(self):
        self.NRC.ping(1)
        self.assertEqual(self.NRC.ping(100), 2)

    def test_add_three_call(self):
        self.NRC.ping(1)
        self.NRC.ping(100)
        self.assertEqual(self.NRC.ping(3001), 3)

    def test_add_four_call(self):
        self.NRC.ping(1)
        self.NRC.ping(100)
        self.NRC.ping(3001)
        self.assertEqual(self.NRC.ping(3002), 3)


if __name__ == "__main__":
    unittest.main()
    