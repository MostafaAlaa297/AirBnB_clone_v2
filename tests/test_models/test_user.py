#!/usr/bin/env python3
"""
================
Test user module
================
"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    def test_create_instance(self):
        user = User()
        self.assertIsInstance(user, User)


if __name__ == "__main__":
    unittest.main()
