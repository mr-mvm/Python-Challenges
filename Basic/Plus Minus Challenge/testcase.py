import unittest
from io import StringIO
import sys
from solution import plusMinus

class TestPlusMinus(unittest.TestCase):
    def capture_output(self, func, *args):
        """
        Captures printed output from a function for testing.
        """
        old_stdout = sys.stdout
        sys.stdout = captured_output = StringIO()
        func(*args)
        sys.stdout = old_stdout
        return captured_output.getvalue().strip().split('\n')

    def test_standard_case(self):
        result = self.capture_output(plusMinus, [-4, 3, -9, 0, 4, 1])
        self.assertEqual(result, ["0.500000", "0.333333", "0.166667"])

    def test_all_positive(self):
        result = self.capture_output(plusMinus, [1, 2, 3, 4, 5])
        self.assertEqual(result, ["1.000000", "0.000000", "0.000000"])

    def test_all_negative(self):
        result = self.capture_output(plusMinus, [-1, -2, -3, -4, -5])
        self.assertEqual(result, ["0.000000", "1.000000", "0.000000"])

    def test_with_zeros(self):
        result = self.capture_output(plusMinus, [0, 0, 0, -1, 1])
        self.assertEqual(result, ["0.200000", "0.200000", "0.600000"])

    def test_empty_array(self):
        result = self.capture_output(plusMinus, [])
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()
