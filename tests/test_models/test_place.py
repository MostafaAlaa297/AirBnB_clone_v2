#!/usr/bin/env python3
"""
================
Test place module
================
"""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    def test_create_instance(self):
        place = Place()
        self.assertIsInstance(place, Place)


if __name__ == "__main__":
    unittest.main()
