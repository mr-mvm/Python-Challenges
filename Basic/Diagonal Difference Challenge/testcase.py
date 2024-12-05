import unittest
from solution import diagonalDifference

class TestDiagonalDifference(unittest.TestCase):
    def test_small_matrix(self):
        self.assertEqual(diagonalDifference([[1, 2], [3, 4]]), 0)
        self.assertEqual(diagonalDifference([[5, 1], [2, 5]]), 7)

    def test_large_matrix(self):
        self.assertEqual(diagonalDifference([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 0)
        self.assertEqual(diagonalDifference([[11, 2, 4], [4, 5, 6], [10, 8, -12]]), 15)

    def test_single_element(self):
        self.assertEqual(diagonalDifference([[42]]), 0)

    def test_negative_numbers(self):
        self.assertEqual(diagonalDifference([[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]), 0)

    def test_mixed_numbers(self):
        self.assertEqual(diagonalDifference([[3, 2, 1], [6, 5, 4], [9, 8, 7]]), 0)

if __name__ == "__main__":
    unittest.main()
