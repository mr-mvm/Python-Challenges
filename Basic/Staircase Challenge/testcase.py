import unittest
from io import StringIO
import sys
from solution import staircase

class TestStaircase(unittest.TestCase):
    def capture_output(self, func, *args):
        """
        Captures printed output from a function for testing.
        """
        old_stdout = sys.stdout
        sys.stdout = captured_output = StringIO()
        func(*args)
        sys.stdout = old_stdout
        return captured_output.getvalue().strip()

    def test_staircase_3(self):
        result = self.capture_output(staircase, 3)
        expected_output = "  #\n ##\n###"
        self.assertEqual(result, expected_output)

    def test_staircase_5(self):
        result = self.capture_output(staircase, 5)
        expected_output = "    #\n   ##\n  ###\n ####\n#####"
        self.assertEqual(result, expected_output)

    def test_staircase_1(self):
        result = self.capture_output(staircase, 1)
        expected_output = "#"
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()
