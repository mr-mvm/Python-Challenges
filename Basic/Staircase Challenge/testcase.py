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

    def test_size_3(self):
        result = self.capture_output(staircase, 3)
        self.assertEqual(result, "  #\n ##\n###")

    def test_size_5(self):
        result = self.capture_output(staircase, 5)
        self.assertEqual(result, "    #\n   ##\n  ###\n ####\n#####")

    def test_size_1(self):
        result = self.capture_output(staircase, 1)
        self.assertEqual(result, "#")

    def test_size_0(self):
        result = self.capture_output(staircase, 0)
        self.assertEqual(result, "")

    def test_size_6(self):
        result = self.capture_output(staircase, 6)
        self.assertEqual(result, "     #\n    ##\n   ###\n  ####\n #####\n######")

if __name__ == "__main__":
    unittest.main()
