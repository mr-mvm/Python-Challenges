import unittest
from solution import birthdayCakeCandles

class TestBirthdayCakeCandles(unittest.TestCase):
    def test_standard_case(self):
        self.assertEqual(birthdayCakeCandles([4, 4, 1, 3]), 2)

    def test_all_same_height(self):
        self.assertEqual(birthdayCakeCandles([2, 2, 2, 2]), 4)

    def test_single_candle(self):
        self.assertEqual(birthdayCakeCandles([7]), 1)

    def test_mixed_heights(self):
        self.assertEqual(birthdayCakeCandles([3, 2, 1, 3, 4, 4]), 2)

    def test_large_numbers(self):
        self.assertEqual(birthdayCakeCandles([1000000000, 999999999, 1000000000, 1000000000]), 3)

if __name__ == "__main__":
    unittest.main()
