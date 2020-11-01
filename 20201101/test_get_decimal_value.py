import unittest
from get_decimal_value import *


class GetDecimalValueTest(unittest.TestCase):
    def test_example_one(self):
        head_input_list = [1,0,1]
        head_list = head_list_generater(head_input_list)
        head = head_list[0]
        expected = 5
        self.assertEqual(get_decimal_value(head), expected)

    def test_example_two(self):
        head_input_list = [0]
        head_list = head_list_generater(head_input_list)
        head = head_list[0]
        expected = 0
        self.assertEqual(get_decimal_value(head), expected)

    def test_example_three(self):
        head_input_list = [1]
        head_list = head_list_generater(head_input_list)
        head = head_list[0]
        expected = 1
        self.assertEqual(get_decimal_value(head), expected)

    def test_example_four(self):
        head_input_list = [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]
        head_list = head_list_generater(head_input_list)
        head = head_list[0]
        expected = 18880
        self.assertEqual(get_decimal_value(head), expected)

    def test_example_five(self):
        head_input_list = [0,0]
        head_list = head_list_generater(head_input_list)
        head = head_list[0]
        expected = 0
        self.assertEqual(get_decimal_value(head), expected)


if __name__ == "__main__":
    unittest.main()
