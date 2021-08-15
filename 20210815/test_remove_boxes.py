from remove_boxes import remove_boxes
import unittest


class TestRemoveBoxes(unittest.TestCase):
    def test_example_one(self):
        boxes = [1, 3, 2, 2, 2, 3, 4, 3, 1]
        expected = 23
        self.assertEqual(remove_boxes(boxes), expected)

    def test_example_two(self):
        boxes = [1, 1, 1]
        expected = 9
        self.assertEqual(remove_boxes(boxes), expected)

    def test_example_three(self):
        boxes = [1]
        expected = 1
        self.assertEqual(remove_boxes(boxes), expected)

    def test_example_four(self):
        boxes = [5,8,3,8,4,8,5,7,4,2]
        expected = 18
        self.assertEqual(remove_boxes(boxes), expected)


if __name__ == '__main__':
    unittest.main()
