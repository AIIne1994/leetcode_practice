import unittest
from word_break import *


class WordBreakTest(unittest.TestCase):
    def test_simple_one(self):
        s = "leetcode"
        wordDict = ["leet", "code"]
        expected = True
        self.assertEqual(word_break(s, wordDict), expected)

    def test_repeat_one(self):
        s = "applepenapple"
        wordDict = ["apple", "pen"]
        expected = True
        self.assertEqual(word_break(s, wordDict), expected)

    def test_fail_one(self):
        s = "catsandog"
        wordDict = ["cats", "dog", "sand", "and", "cat"]
        expected = False
        self.assertEqual(word_break(s, wordDict), expected)

    def test_recursive_one(self):
        s = "cars"
        wordDict = ["car","ca","rs"]
        expected = True
        self.assertEqual(word_break(s, wordDict), expected)

    def test_duplicate_character(self):
        s = "aaaaaaa"
        wordDict = ["aaaa","aaa"]
        expected = True
        self.assertEqual(word_break(s, wordDict), expected)

    def test_inside_one(self):
        s = "cbca"
        wordDict = ["bc","ca"]
        expected = False
        self.assertEqual(word_break(s, wordDict), expected)


if __name__ == "__main__":
    unittest.main()
    