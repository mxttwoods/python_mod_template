"""
This demonstrates how to use the unittest framework.
"""

import unittest

from sample import get_answer, get_hmm, hmm


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_thoughts(self):
        self.assertIsNone(hmm())

    def test_answer(self):
        self.assertTrue(get_answer())

    def test_hmm(self):
        self.assertEqual(get_hmm(), "hmmm...")


if __name__ == "__main__":
    unittest.main()
