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

    def square_root(self, x):
        if x < 0:
            raise ValueError("Cannot take square root of negative number")
        result = math.sqrt(x)
        self.history.append(f"√{x} = {result}")
        return result

    def factorial(self, n):
        if not isinstance(n, int):
            raise ValueError("Factorial is only defined for integers")
        if n < 0:
            raise ValueError("Cannot take factorial of negative number")
        result = math.factorial(n)
        self.history.append(f"{n}! = {result}")
        return result

    def percentage(self, total, percent):
        result = (total * percent) / 100
        self.history.append(f"{percent}% of {total} = {result}")
        return result

    def get_history(self):
        return self.history

    def clear_history(self):
        self.history.clear()
