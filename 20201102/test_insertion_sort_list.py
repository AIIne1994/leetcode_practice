import unittest
from insertion_sort_list import *


class InsertionSortListTest(unittest.TestCase):
    def test_example_one(self):
        head_input_list = [4,2,1,3]
        head_list = head_list_generater(head_input_list)
        head = head_list[0]
        expected = 5
        self.assertEqual(insertion_sort_list(head), expected)

    def test_example_two(self):
        head_input_list = [0]
        head_list = head_list_generater(head_input_list)
        head = head_list[0]
        expected = 0
        self.assertEqual(insertion_sort_list(head), expected)


if __name__ == "__main__":
    unittest.main()
