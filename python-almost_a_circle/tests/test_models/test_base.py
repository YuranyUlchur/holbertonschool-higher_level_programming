#!/usr/bin/python3
"""
    Module of unit tests for the Base class.
"""
import unittest
from models.base import Base

basetest1 = Base()
basetest2 = Base(89)


class TestBase(unittest.TestCase):
    """These tests ensure that the Base class behaves
    correctly and has the expected functionality."""

    def test_contructor(self):
        """Test that a new instance of Base can be created
        and is an instance of the Base class."""
        self.assertIsInstance(basetest1, Base)

    def test_id_none(self):
        """Test of Base() for assigning automatically
        an ID + 1 of the previous exists"""
        self.assertEqual(basetest1.id, 1)

    def test_assignment_id(self):
        """Verify that the id passed to the instance is equal to"""
        self.assertEqual(basetest2.id, 89)

    def test_to_json_string(self):
        """Test verifies that the method exists"""
        list = basetest2.to_json_string(None)
        self.assertEqual(list, [])

    def test_from_json_string(self):
        list = basetest2.from_json_string(None)
        self.assertEqual(list, [])

if __name__ == '__main__':
    unittest.main()
