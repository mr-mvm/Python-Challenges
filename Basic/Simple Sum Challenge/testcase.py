import unittest
from solution import solveMeFirst

class TestSolveMeFirst(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(solveMeFirst(3, 7), 10)
        self.assertEqual(solveMeFirst(100, 200), 300)

    def test_negative_numbers(self):
        self.assertEqual(solveMeFirst(-5, -10), -15)
        self.assertEqual(solveMeFirst(-1, 1), 0)

    def test_zero(self):
        self.assertEqual(solveMeFirst(0, 0), 0)
        self.assertEqual(solveMeFirst(0, 5), 5)

    def test_large_numbers(self):
        self.assertEqual(solveMeFirst(123456, 654321), 777777)

if __name__ == "__main__":
    # Run all test cases
    unittest.main()
