import unittest
from solution import timeConversion

class TestTimeConversion(unittest.TestCase):
    def test_midnight(self):
        self.assertEqual(timeConversion("12:00:00AM"), "00:00:00")

    def test_noon(self):
        self.assertEqual(timeConversion("12:00:00PM"), "12:00:00")

    def test_am_time(self):
        self.assertEqual(timeConversion("07:05:45AM"), "07:05:45")
        self.assertEqual(timeConversion("01:59:59AM"), "01:59:59")

    def test_pm_time(self):
        self.assertEqual(timeConversion("07:05:45PM"), "19:05:45")
        self.assertEqual(timeConversion("11:59:59PM"), "23:59:59")

if __name__ == '__main__':
    unittest.main()
