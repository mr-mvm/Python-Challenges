import unittest
from solution import aVeryBigSum

class TestAVeryBigSum(unittest.TestCase):
    def test_standard_case(self):
        self.assertEqual(aVeryBigSum([1000000001, 1000000002, 1000000003, 1000000004, 1000000005]), 5000000015)

    def test_single_element(self):
        self.assertEqual(aVeryBigSum([123456789]), 123456789)

    def test_all_zeros(self):
        self.assertEqual(aVeryBigSum([0, 0, 0, 0, 0]), 0)

    def test_large_numbers(self):
        self.assertEqual(aVeryBigSum([999999999, 999999999, 999999999]), 2999999997)

    def test_mixed_numbers(self):
        self.assertEqual(aVeryBigSum([-1, 0, 1, 2, -2]), 0)

if __name__ == '__main__':
    unittest.main()
