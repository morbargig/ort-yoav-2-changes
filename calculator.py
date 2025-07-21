"""
Calculator Class for Student Practice

This module contains a Calculator class with methods that students need to implement.
Each method has a docstring explaining what it should do and includes examples.

Students should implement the methods marked with "TODO" comments.
"""


class Calculator:
    """
    A simple calculator class for basic mathematical operations.

    This class provides methods for basic arithmetic operations and some
    advanced mathematical functions. Students should implement each method
    according to the specifications in the docstrings.
    """

    def __init__(self):
        """Initialize the calculator."""
        self.history = []  # Store calculation history

    def add(self, a, b):
        return (a+b)

        """
        Add two numbers together.

        Args:
            a (float): First number
            b (float): Second number

        Returns:
            float: The sum of a and b

        Example:
            >>> calc = Calculator()
            >>> calc.add(2, 3)
            5
        """
        # TODO: Implement addition
        # Hint: Store the operation in self.history as a string
        pass

    def subtract(self, a, b):
        return (a-b)
        """
        Subtract the second number from the first.

        Args:
            a (float): First number
            b (float): Second number

        Returns:
            float: The difference of a and b (a - b)

        Example:
            >>> calc = Calculator()
            >>> calc.subtract(5, 3)
            2
        """
        # TODO: Implement subtraction
        pass

    def multiply(self, a, b):
        return (a*b)
        """
        Multiply two numbers.

        Args:
            a (float): First number
            b (float): Second number

        Returns:
            float: The product of a and b

        Example:
            >>> calc = Calculator()
            >>> calc.multiply(4, 3)
            12
        """
        # TODO: Implement multiplication
        pass

    def divide(self, a, b):
        return (a/b)
        """
        Divide the first number by the second.

        Args:
            a (float): Dividend
            b (float): Divisor

        Returns:
            float: The quotient of a and b (a / b)

        Raises:
            ValueError: If b is zero (division by zero)

        Example:
            >>> calc = Calculator()
            >>> calc.divide(8, 2)
            4.0
            >>> calc.divide(5, 0)
            Traceback (most recent call last):
            ...
            ValueError: Cannot divide by zero
        """
        # TODO: Implement division
        # Remember to check for division by zero!
        pass

    def power(self, base, exponent):
        return (base**exponent)
        """
        Raise a number to a power.

        Args:
            base (float): The base number
            exponent (float): The exponent

        Returns:
            float: base raised to the power of exponent

        Example:
            >>> calc = Calculator()
            >>> calc.power(2, 3)
            8
            >>> calc.power(9, 0.5)
            3.0
        """
        # TODO: Implement exponentiation
        pass

    def square_root(self, number):
        return (number**0.5)
    """"
        Calculate the square root of a number.

        Args:
            number(float): The number to find square root of

        Returns:
            float: The square root of the number

        Raises:
            ValueError: If number is negative

        Example:
            >> > calc = Calculator()
            >> > calc.square_root(16)
            4.0
            >> > calc.square_root(-1)
            Traceback(most recent call last):
            ...
            ValueError: Cannot calculate square root of negative number
        """
    # TODO: Implement square root
    # Hint: You can use number ** 0.5 or import math and use math.sqrt()
    pass

    def factorial(self, n):
        """
        Calculate the factorial of a non-negative integer.

        Args:
            n(int): The number to calculate factorial of

        Returns:
            int: The factorial of n(n!)

        Raises:
            ValueError: If n is negative or not an integer

        Example:
            >> > calc = Calculator()
            >> > calc.factorial(5)
            120
            >> > calc.factorial(0)
            1
        """
        # TODO: Implement factorial
        # Remember: 0! = 1, and factorial is only defined for non-negative integers
        pass

    def percentage(self, value, percent):
        """
        Calculate what percentage of a value.

        Args:
            value(float): The total value
            percent(float): The percentage to calculate

        Returns:
            float: The percentage of the value

        Example:
            >> > calc = Calculator()
            >> > calc.percentage(100, 25)
            25.0
            >> > calc.percentage(80, 12.5)
            10.0
        """
        # TODO: Implement percentage calculation
        pass

    def get_history(self):
        """
        Get the calculation history.

        Returns:
            list: List of calculation strings

        Example:
            >> > calc = Calculator()
            >> > calc.add(2, 3)
            5
            >> > calc.multiply(4, 5)
            20
            >> > calc.get_history()
            ['2 + 3 = 5', '4 * 5 = 20']
        """
        return self.history.copy()

    def clear_history(self):
        """
        Clear the calculation history.

        Example:
            >> > calc = Calculator()
            >> > calc.add(1, 1)
            2
            >> > calc.clear_history()
            >> > calc.get_history()
            []
        """
        self.history.clear()
