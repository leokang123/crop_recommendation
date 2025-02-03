"""
Example tests
"""
from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """Test calc module"""
    """function name should be start with "test_"""

    def test_add_numbers(self):
        """Test adding numbers together"""
        res = calc.add(5, 8)
        self.assertEqual(res, 13)

    def test_subtract_numbers(self):
        """Test subtracting numbers"""
        res = calc.subtract(10, 15)
        self.assertEqual(res, -5)
