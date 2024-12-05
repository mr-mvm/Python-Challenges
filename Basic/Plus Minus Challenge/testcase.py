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
        return captured_output.getvalue().strip()

    def test_all_positive(self):
        result = self.capture_output(plusMinus, [1, 2, 3, 4, 5])
        self.assertEqual(result, "1.000000\n0.000000\n0.000000")

    def test_all_negative(self):
        result = self.capture_output(plusMinus, [-1, -2, -3])
        self.assertEqual(result, "0.000000\n1.000000\n0.000000")

    def test_all_zero(self):
        result = self.capture_output(plusMinus, [0, 0, 0])
        self.assertEqual(result, "0.000000\n0.000000\n1.000000")

    def test_mixed(self):
        result = self.capture_output(plusMinus, [-4, 3, -9, 0, 4, 1])
        self.assertEqual(result, "0.500000\n0.333333\n0.166667")

    def test_single_element(self):
        result = self.capture_output(plusMinus, [0])
        self.assertEqual(result, "0.000000\n0.000000\n1.000000")

if __name__ == "__main__":
    unittest.main()
