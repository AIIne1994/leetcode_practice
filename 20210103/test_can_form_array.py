from can_form_array import canFormArray
import unittest


class TestCanFormArray(unittest.TestCase):
    def test_example_one(self):
        arr = [85]
        pieces = [[85]]
        expected = True
        self.assertEqual(canFormArray(arr, pieces), expected)

    def test_example_two(self):
        arr = [15, 88]
        pieces = [[88], [15]]
        expected = True
        self.assertEqual(canFormArray(arr, pieces), expected)

    def test_example_three(self):
        arr = [49, 18, 16]
        pieces = [[16, 18, 49]]
        expected = False
        self.assertEqual(canFormArray(arr, pieces), expected)

    def test_example_four(self):
        arr = [91, 4, 64, 78]
        pieces = [[78], [4, 64], [91]]
        expected = True
        self.assertEqual(canFormArray(arr, pieces), expected)

    def test_example_five(self):
        arr = [1, 3, 5, 7]
        pieces = [[2, 4, 6, 8]]
        expected = False
        self.assertEqual(canFormArray(arr, pieces), expected)

    def test_example_six(self):
        arr = [1,2,3]
        pieces = [[2],[1,3]]
        expected = False
        self.assertEqual(canFormArray(arr, pieces), expected)


if __name__ == '__main__':
    unittest.main()
