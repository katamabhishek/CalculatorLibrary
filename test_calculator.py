"""
Unit tests for the calculator library
"""

import calculator


class TestCalculator:

    def test_addition(self):
        assert 5 == calculator.add(2, 3)

    def test_subtraction(self):
        assert 2 == calculator.subtract(4, 2)

    def test_multiply(self):
        assert 6 == calculator.multiply(2,3)
