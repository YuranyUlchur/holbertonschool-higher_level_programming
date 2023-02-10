#!/usr/bin/python3
'''max integer'''

import unittest

max_integer = __import__("6-max_integer").max_integer
'''unittest for the functions of max integer'''


class MaxInteger(unittest.TestCase):
    def test_cases(self):
        '''tests basic for the functions max integer'''
        self.assertEqual(max_integer([3, 10, 30, 50]), 50)
        self.assertEqual(max_integer([-3, -10, -30, -50]), -3)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([-3, 10, 30, 70]), 70)
        self.assertEqual(max_integer([90]), 90)

    def test_error(self):
        """Tests for error"""
        self.assertRaises(TypeError, max_integer, None)
        self.assertRaises(TypeError, max_integer, 7856)
