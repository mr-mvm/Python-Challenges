import unittest
from solution import simpleArraySum

class TestSimpleArraySum(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(simpleArraySum([1, 2, 3, 4, 5]), 15)
        self.assertEqual(simpleArraySum([10, 20, 30]), 60)

    def test_negative_numbers(self):
        self.assertEqual(simpleArraySum([-1, -2, -3]), -6)
        self.assertEqual(simpleArraySum([-10, -20, 30]), 0)

    def test_mixed_numbers(self):
        self.assertEqual(simpleArraySum([0, 0, 0]), 0)
        self.assertEqual(simpleArraySum([10, -5, 15]), 20)

    def test_empty_array(self):
        self.assertEqual(simpleArraySum([]), 0)

    def test_large_numbers(self):
        self.assertEqual(simpleArraySum([1000000, 2000000, 3000000]), 6000000)

if __name__ == "__main__":
    unittest.main()
