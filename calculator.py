"""
Simple Calculator Class - Student Implementation Required

Students need to implement all the methods below.
"""


class Calculator:
    def __init__(self):
        self.history = []

    def add(self, a, b):
        """Add two numbers"""
        return a + b

        # TODO: Implement addition
        # Hint: result = a + b, then add to history
        pass

    def subtract(self, a, b):
        """Subtract b from a"""
        # TODO: Implement subtraction
        return a - b

    def multiply(self, a, b):
        # TODO: Implement multiplication
        pass

    def divide(self, a, b):
        # TODO: Implement division
        pass
    def get_history(self):     
        """Return calculation history"""
        return self.history

    def clear_history(self):
        """Clear calculation history"""
        self.history = []
