import math

class Calculator:
    def __init__(self):
        self.history = []

    def add(self, a, b):
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result

    def subtract(self, a, b):
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result

    def multiply(self, a, b):
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result

    def power(self, base, exponent):
        result = base ** exponent
        self.history.append(f"{base} ^ {exponent} = {result}")
        return result

    def square_root(self, number):
        if number < 0:
            raise ValueError("Cannot calculate square root of negative number")
        result = math.sqrt(number)
        self.history.append(f"√{number} = {result}")
        return result

    def factorial(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError("Factorial is only defined for non-negative integers")
        result = math.factorial(n)
        self.history.append(f"{n}! = {result}")
        return result

    def percentage(self, value, percent):
        result = (value * percent) / 100
        self.history.append(f"{percent}% of {value} = {result}")
        return result

    def get_history(self):
        return self.history.copy()

    def clear_history(self):
        self.history.clear()
