#!/usr/bin/env python3
"""
================
Test review module
================
"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    def test_create_instance(self):
        review = Review()
        self.assertIsInstance(review, Review)


if __name__ == "__main__":
    unittest.main()
