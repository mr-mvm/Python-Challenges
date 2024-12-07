import unittest
from solution import solveMeFirst

class TestSolveMeFirst(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(solveMeFirst(5, 7), 12)

    def test_negative_numbers(self):
        self.assertEqual(solveMeFirst(-3, -6), -9)

    def test_mixed_sign_numbers(self):
        self.assertEqual(solveMeFirst(4, -2), 2)

    def test_zero(self):
        self.assertEqual(solveMeFirst(0, 0), 0)

    def test_large_numbers(self):
        self.assertEqual(solveMeFirst(1000000, 2000000), 3000000)

if __name__ == "__main__":
    unittest.main()
