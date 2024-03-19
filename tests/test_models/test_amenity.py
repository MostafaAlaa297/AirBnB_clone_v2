#!/usr/bin/env python3
"""
================
Test amenity module
================
"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    def test_create_instance(self):
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)


if __name__ == "__main__":
    unittest.main()
