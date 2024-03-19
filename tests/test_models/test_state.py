#!/usr/bin/env python3
"""
================
Test state module
================
"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    def test_create_instance(self):
        state = State()
        self.assertIsInstance(state, State)


if __name__ == "__main__":
    unittest.main()
