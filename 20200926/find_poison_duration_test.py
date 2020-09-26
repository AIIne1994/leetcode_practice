import unittest
from find_poison_duration import *

class FindPoisonDurationTest(unittest.TestCase):
    def test_full_damage_with_two_attacks(self):
        times = [1, 4]
        duration = 2
        expected = 4
        self.assertEqual(findPoisonedDuration(times, duration), expected)

    def test_damage_with_two_attacks(self):
        times = [1, 2]
        duration = 2
        expected = 3
        self.assertEqual(findPoisonedDuration(times, duration), expected)


if __name__ == "__main__":
    unittest.main()
