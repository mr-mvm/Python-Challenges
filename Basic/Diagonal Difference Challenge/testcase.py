import unittest
from solution import diagonalDifference

class TestDiagonalDifference(unittest.TestCase):
    def test_standard_case(self):
        self.assertEqual(diagonalDifference([[11, 2, 4], [4, 5, 6], [10, 8, -12]]), 15)

    def test_zero_matrix(self):
        self.assertEqual(diagonalDifference([[0, 0, 0], [0, 0, 0], [0, 0, 0]]), 0)

    def test_single_element(self):
        self.assertEqual(diagonalDifference([[5]]), 0)

    def test_negative_numbers(self):
        self.assertEqual(diagonalDifference([[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]), 0)

    def test_large_matrix(self):
        self.assertEqual(
            diagonalDifference([
                [1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 16]
            ]),
            0
        )

if __name__ == '__main__':
    unittest.main()
