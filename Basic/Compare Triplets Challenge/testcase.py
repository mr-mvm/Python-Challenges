import unittest
from solution import compareTriplets

class TestCompareTriplets(unittest.TestCase):
    def test_standard_case(self):
        self.assertEqual(compareTriplets([5, 6, 7], [3, 6, 10]), [1, 1])

    def test_all_equal(self):
        self.assertEqual(compareTriplets([5, 5, 5], [5, 5, 5]), [0, 0])

    def test_alice_wins_all(self):
        self.assertEqual(compareTriplets([10, 20, 30], [1, 2, 3]), [3, 0])

    def test_bob_wins_all(self):
        self.assertEqual(compareTriplets([1, 2, 3], [10, 20, 30]), [0, 3])

    def test_mixed_scores(self):
        self.assertEqual(compareTriplets([4, 7, 9], [5, 7, 6]), [1, 1])

if __name__ == '__main__':
    unittest.main()
