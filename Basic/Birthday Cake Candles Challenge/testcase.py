import unittest
from solution import birthdayCakeCandles

class TestBirthdayCakeCandles(unittest.TestCase):
    def test_standard_case(self):
        self.assertEqual(birthdayCakeCandles([4, 4, 1, 3]), 2)

    def test_all_same_height(self):
        self.assertEqual(birthdayCakeCandles([3, 3, 3, 3]), 4)

    def test_one_tallest_candle(self):
        self.assertEqual(birthdayCakeCandles([1, 2, 3, 4, 5]), 1)

    def test_large_numbers(self):
        self.assertEqual(birthdayCakeCandles([1000000, 1000000, 999999]), 2)

    def test_single_candle(self):
        self.assertEqual(birthdayCakeCandles([1]), 1)

if __name__ == '__main__':
    unittest.main()
