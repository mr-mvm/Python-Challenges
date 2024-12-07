import unittest
from solution import simpleArraySum

class TestSimpleArraySum(unittest.TestCase):
    def test_standard_case(self):
        self.assertEqual(simpleArraySum([1, 2, 3, 4, 10, 11]), 31)

    def test_empty_array(self):
        self.assertEqual(simpleArraySum([]), 0)

    def test_single_element(self):
        self.assertEqual(simpleArraySum([5]), 5)

    def test_negative_numbers(self):
        self.assertEqual(simpleArraySum([-1, -2, -3, -4, -5]), -15)

    def test_large_numbers(self):
        self.assertEqual(simpleArraySum([1000000, 1000000, 1000000]), 3000000)

if __name__ == '__main__':
    unittest.main()
