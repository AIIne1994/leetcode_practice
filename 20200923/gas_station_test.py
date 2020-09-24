import unittest
from gas_station import *

class GasStationTest(unittest.TestCase):
    def test_can_complete_circuit(self):
        gas = [1, 2, 3, 4, 5]
        cost = [3, 4, 5, 1, 2]
        expected = 3
        self.assertEqual(canCompleteCircuit(gas, cost), expected)

    def test_cannot_complete_circuit(self):
        gas = [2, 3, 4]
        cost = [3, 4, 3]
        expected = -1
        self.assertEqual(canCompleteCircuit(gas, cost), expected)

    def test_another_can_complete_circuit(self):
        gas = [5, 1, 2, 3, 4]
        cost = [4, 4, 1, 5, 1]
        expected = 4
        self.assertEqual(canCompleteCircuit(gas, cost), expected)

    def test_can_complete_circuit_with_same_gas(self):
        gas = [5, 8, 2, 8]
        cost = [6, 5, 6, 6]
        expected = 3
        self.assertEqual(canCompleteCircuit(gas, cost), expected)

    def test_can_complete_circuit_with_start_at_the_end_of_list(self):
        gas = [3, 1, 1]
        cost = [1, 2, 2]
        expected = 0
        self.assertEqual(canCompleteCircuit(gas, cost), expected)


if __name__ == "__main__":
    unittest.main()
    