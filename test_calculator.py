"""
Test file for Calculator class

This file contains tests that students can run to verify their implementations.
Run tests with: python -m pytest test_calculator.py

Students should implement all methods in calculator.py before running these tests.
"""

import pytest
from calculator import Calculator


class TestCalculator:
    """Test cases for the Calculator class."""
    
    def setup_method(self):
        """Create a fresh calculator instance for each test."""
        self.calc = Calculator()
    
    def test_add(self):
        """Test addition method."""
        assert self.calc.add(2, 3) == 5
        assert self.calc.add(-1, 1) == 0
        assert self.calc.add(0.1, 0.2) == pytest.approx(0.3)
        assert self.calc.add(-5, -3) == -8
    
    def test_subtract(self):
        """Test subtraction method."""
        assert self.calc.subtract(5, 3) == 2
        assert self.calc.subtract(1, 1) == 0
        assert self.calc.subtract(-1, -1) == 0
        assert self.calc.subtract(0, 5) == -5
    
    def test_multiply(self):
        """Test multiplication method."""
        assert self.calc.multiply(4, 3) == 12
        assert self.calc.multiply(-2, 3) == -6
        assert self.calc.multiply(0, 100) == 0
        assert self.calc.multiply(2.5, 4) == 10.0
    
    def test_divide(self):
        """Test division method."""
        assert self.calc.divide(8, 2) == 4.0
        assert self.calc.divide(9, 3) == 3.0
        assert self.calc.divide(1, 3) == pytest.approx(0.3333333333333333)
        assert self.calc.divide(-10, 2) == -5.0
    
    def test_divide_by_zero(self):
        """Test that division by zero raises ValueError."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            self.calc.divide(5, 0)
    
    def test_power(self):
        """Test exponentiation method."""
        assert self.calc.power(2, 3) == 8
        assert self.calc.power(5, 0) == 1
        assert self.calc.power(9, 0.5) == pytest.approx(3.0)
        assert self.calc.power(-2, 2) == 4
    
    def test_square_root(self):
        """Test square root method."""
        assert self.calc.square_root(16) == 4.0
        assert self.calc.square_root(25) == 5.0
        assert self.calc.square_root(2) == pytest.approx(1.4142135623730951)
        assert self.calc.square_root(0) == 0.0
    
    def test_square_root_negative(self):
        """Test that square root of negative number raises ValueError."""
        with pytest.raises(ValueError, match="Cannot calculate square root of negative number"):
            self.calc.square_root(-1)
    
    def test_factorial(self):
        """Test factorial method."""
        assert self.calc.factorial(0) == 1
        assert self.calc.factorial(1) == 1
        assert self.calc.factorial(5) == 120
        assert self.calc.factorial(3) == 6
    
    def test_factorial_negative(self):
        """Test that factorial of negative number raises ValueError."""
        with pytest.raises(ValueError):
            self.calc.factorial(-1)
    
    def test_factorial_non_integer(self):
        """Test that factorial of non-integer raises ValueError."""
        with pytest.raises(ValueError):
            self.calc.factorial(3.5)
    
    def test_percentage(self):
        """Test percentage calculation method."""
        assert self.calc.percentage(100, 25) == 25.0
        assert self.calc.percentage(80, 12.5) == 10.0
        assert self.calc.percentage(200, 50) == 100.0
        assert self.calc.percentage(50, 0) == 0.0
    
    def test_history_tracking(self):
        """Test that calculations are stored in history."""
        # Perform some calculations
        self.calc.add(2, 3)
        self.calc.multiply(4, 5)
        self.calc.divide(10, 2)
        
        # Check history
        history = self.calc.get_history()
        assert len(history) == 3
        assert "2 + 3 = 5" in history
        assert "4 * 5 = 20" in history
        assert "10 / 2 = 5.0" in history
    
    def test_clear_history(self):
        """Test clearing calculation history."""
        # Add some calculations
        self.calc.add(1, 1)
        self.calc.subtract(3, 1)
        
        # Verify history has items
        assert len(self.calc.get_history()) == 2
        
        # Clear history
        self.calc.clear_history()
        
        # Verify history is empty
        assert len(self.calc.get_history()) == 0


def test_calculator_creation():
    """Test that Calculator can be instantiated."""
    calc = Calculator()
    assert calc is not None
    assert calc.get_history() == []


if __name__ == "__main__":
    # Allow running tests directly with python test_calculator.py
    pytest.main([__file__]) 