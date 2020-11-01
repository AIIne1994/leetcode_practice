import unittest
from recover_tree import *

class RecoveredTreeTest(unittest.TestCase):
    def test_example_one(self):
        root = [1, 3, null, null, 2]
        expected = [3, 1, null, null, 2]
        recoverTree(root)
        self.assertEqual(root, expected)

    def test_example_two(self):
        root = [3, 1, 4, null, null, 2]
        expected = [2, 1, 4, null, null, 3]
        recoverTree(root)
        self.assertEqual(root, expected)



if __name__ == "__main__":
    unittest.main()
