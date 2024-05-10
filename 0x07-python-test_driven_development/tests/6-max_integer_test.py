#!/usr/bin/python3
"""Unittest for max_integer function from a module.
"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Defines comprehensive test cases for the max_integer function."""

    def test_empty_default_argument(self):
        """Test when no argument is passed."""
        self.assertIsNone(max_integer())

    def test_empty_list(self):
        """Test passing an empty list."""
        self.assertIsNone(max_integer([]))

    def test_single_element(self):
        """Test a list with a single element."""
        self.assertEqual(max_integer([98]), 98)

    def test_all_identical_elements(self):
        """Test a list where all elements are the same."""
        self.assertEqual(max_integer([7, 7, 7, 7]), 7)

    def test_maximum_at_start(self):
        """Test a list where the maximum element is at the start."""
        self.assertEqual(max_integer([50, 20, 10]), 50)

    def test_maximum_at_end(self):
        """Test a list where the maximum element is at the end."""
        self.assertEqual(max_integer([10, 20, 50]), 50)

    def test_with_mixed_order(self):
        """Test a list with elements in no specific order."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_with_large_numbers(self):
        """Test a list with large integers."""
        self.assertEqual(max_integer([500, 1000, 750, 1200]), 1200)

    def test_with_positive_and_negative(self):
        """Test a list containing both positive and negative numbers."""
        self.assertEqual(max_integer([-100, 1, 2, 3, -50]), 3)

    def test_with_all_negative_numbers(self):
        """Test a list of all negative numbers."""
        self.assertEqual(max_integer([-10, -22, -3]), -3)

    def test_with_floats_and_integers(self):
        """Test a list with both integers and floating-point numbers."""
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)

    def test_with_string_argument(self):
        """Test passing a string instead of a list."""
        self.assertEqual(max_integer("holberton"), 't')

    def test_with_list_of_strings(self):
        """Test passing a list of strings."""
        self.assertEqual(max_integer(["apple", "banana", "cherry"]), "cherry")

    def test_with_none(self):
        """Test passing None as an argument."""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_with_different_types(self):
        """Test passing a list with mixed data types."""
        with self.assertRaises(TypeError):
            max_integer([1, "string", 3.14])

    def test_with_inf_values(self):
        """Test a list with infinite values."""
        self.assertEqual(max_integer([1, float('inf'), 3, float('-inf')]), float('inf'))

    def test_with_nan_values(self):
        """Test a list containing NaN values."""
        self.assertEqual(max_integer([1, float('nan'), 2]), 2)

if __name__ == '__main__':
    unittest.main()
