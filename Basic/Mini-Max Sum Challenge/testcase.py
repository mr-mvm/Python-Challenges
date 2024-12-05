import unittest
from io import StringIO
import sys
from solution import miniMaxSum

class TestMiniMaxSum(unittest.TestCase):
    def capture_output(self, func, *args):
        """
        Captures printed output from a function for testing.
        """
        old_stdout = sys.stdout
        sys.stdout = captured_output = StringIO()
        func(*args)
        sys.stdout = old_stdout
        return captured_output.getvalue().strip()

    def test_standard_case(self):
        result = self.capture_output(miniMaxSum, [1, 2, 3, 4, 5])
        self.assertEqual(result, "10 14")

    def test_all_same(self):
        result = self.capture_output(miniMaxSum, [7, 7, 7, 7, 7])
        self.assertEqual(result, "28 28")

    def test_negative_numbers(self):
        result = self.capture_output(miniMaxSum, [-1, -2, -3, -4, -5])
        self.assertEqual(result, "-14 -10")

    def test_mixed_numbers(self):
        result = self.capture_output(miniMaxSum, [0, 1, 2, 3, 4])
        self.assertEqual(result, "6 10")

    def test_large_numbers(self):
        result = self.capture_output(miniMaxSum, [1000000000, 1000000000, 1000000000, 1000000000, 1000000000])
        self.assertEqual(result, "4000000000 4000000000")

if __name__ == "__main__":
    unittest.main()
