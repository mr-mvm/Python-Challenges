import unittest
from solution import aVeryBigSum

class TestAVeryBigSum(unittest.TestCase):
    def test_small_numbers(self):
        self.assertEqual(aVeryBigSum([1, 2, 3, 4, 5]), 15)
        self.assertEqual(aVeryBigSum([10, 20, 30]), 60)

    def test_large_numbers(self):
        self.assertEqual(aVeryBigSum([1000000000, 2000000000, 3000000000]), 6000000000)
        self.assertEqual(aVeryBigSum([9223372036854775807, 1]), 9223372036854775808)

    def test_empty_list(self):
        self.assertEqual(aVeryBigSum([]), 0)

    def test_mixed_numbers(self):
        self.assertEqual(aVeryBigSum([10, -5, 15, -5]), 15)

if __name__ == "__main__":
    unittest.main()
