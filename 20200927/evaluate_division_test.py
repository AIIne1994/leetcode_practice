import unittest
from evaluate_division import *

class EvaluateDivisionTest(unittest.TestCase):
    def test_two_equations_five_queries(self):
        equations = [["a","b"],["b","c"]]
        values = [2.0, 3.0]
        queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
        expected = [6.00000,0.50000,-1.00000,1.00000,-1.00000]
        self.assertEqual(calcEquation(equations, values, queries), expected)

    def test_three_equations_four_queries(self):
        equations = [["a","b"],["b","c"],["bc","cd"]]
        values = [1.5,2.5,5.0]
        queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
        expected = [3.75000,0.40000,5.00000,0.20000]
        self.assertEqual(calcEquation(equations, values, queries), expected)

    def test_one_equation_four_queries(self):
        equations = [["a","b"]]
        values = [0.5]
        queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
        expected = [0.50000,2.00000,-1.00000,-1.00000]
        self.assertEqual(calcEquation(equations, values, queries), expected)


if __name__ == "__main__":
    unittest.main()
    