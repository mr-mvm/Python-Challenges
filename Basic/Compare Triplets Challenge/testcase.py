import unittest
from solution import compareTriplets

class TestCompareTriplets(unittest.TestCase):
    def test_equal_scores(self):
        self.assertEqual(compareTriplets([5, 6, 7], [5, 6, 7]), [0, 0])

    def test_alice_wins(self):
        self.assertEqual(compareTriplets([10, 20, 30], [5, 15, 25]), [3, 0])

    def test_bob_wins(self):
        self.assertEqual(compareTriplets([1, 2, 3], [4, 5, 6]), [0, 3])

    def test_mixed_results(self):
        self.assertEqual(compareTriplets([1, 2, 3], [3, 2, 1]), [1, 1])

    def test_partial_scores(self):
        self.assertEqual(compareTriplets([6, 7, 8], [6, 8, 7]), [1, 1])

if __name__ == "__main__":
    unittest.main()
