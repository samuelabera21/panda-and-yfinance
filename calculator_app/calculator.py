class Calculator:
    def __init__(self):
        self._history = []

    def add(self, a, b):
        result = a + b
        self._save_history(a, "+", b, result)
        return result

    def subtract(self, a, b):
        result = a - b
        self._save_history(a, "-", b, result)
        return result

    def multiply(self, a, b):
        result = a * b
        self._save_history(a, "*", b, result)
        return result

    def divide(self, a, b):
        if b == 0:
            return "Cannot divide by zero"
        result = a / b
        self._save_history(a, "/", b, result)
        return result

    def _save_history(self, a, operator, b, result):
        self._history.append(f"{a} {operator} {b} = {result}")

    def get_history(self):
        return self._history
