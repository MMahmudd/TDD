import unittest
from my_math import add_numbers

class MyMathTestCase(unittest.TestCase):
    def test_add_numbers(self):
        result = add_numbers(3, 4)
        self.assertEqual(result, 7)

        result = add_numbers(-1, 1)
        self.assertEqual(result, 0)

        result = add_numbers(0, 0)
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()
