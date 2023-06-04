# test_calculator.py

import unittest
from calculator import add, subtract

class CalculatorTestCase(unittest.TestCase):
    def test_add(self):
        result = add(3, 4)
        self.assertEqual(result, 7)

        result = add(-1, 1)
        self.assertEqual(result, 0)

        result = add(0, 0)
        self.assertEqual(result, 0)

    def test_subtract(self):
        result = subtract(5, 2)
        self.assertEqual(result, 3)

        result = subtract(10, 5)
        self.assertEqual(result, 5)

if __name__ == '__main__':
    unittest.main()
