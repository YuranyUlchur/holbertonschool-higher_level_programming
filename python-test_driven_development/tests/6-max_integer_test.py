import unittest

max_integer = __import__("6-max_integer").max_integer
'''unittest for the functions of max integer'''


class MaxInteger(unittest.TestCase):
    def max_integer(self):
        '''tests basic for the functions max integer'''
        self.assertEqual(max_integer([3, 10, 30, 50]), 50)
        self.assertEqual(max_integer([-3, -10, -30, -50]), -3)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([-3, 10, 30, 70]), 70)

    def test_error(self):
        """Tests for error"""
        self.assertRaises(TypeError, max_integer, None)
        self.assertRaises(TypeError, max_integer, 7856)
