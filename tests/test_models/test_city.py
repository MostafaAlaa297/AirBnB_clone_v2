#!/usr/bin/env python3
"""
================
Test city module
================
"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    def test_create_instance(self):
        city = City()
        self.assertIsInstance(city, City)


if __name__ == "__main__":
    unittest.main()
