import unittest
from majority_element_ii import *

class MajorityElementIITest(unittest.TestCase):
    def test_three_elements_list_with_one_majority(self):
        testing_input = [3,2,3]
        expected = [3]
        self.assertEqual(majorityElement(testing_input), expected)

    def test_two_trips_with_capacity_with_five(self):
        testing_input = [1,1,1,3,3,2,2,2]
        expected = [1,2]
        self.assertEqual(majorityElement(testing_input), expected)


if __name__ == "__main__":
    unittest.main()
    