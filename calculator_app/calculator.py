class Calculator:
    def __init__(self):
        self._history = []

    def add(self, a, b):
        if not self._is_valid_number(a, b):
            return "Please enter numeric values only"
        result = a + b
        self._save_history(a, "+", b, result)
        return result

    def subtract(self, a, b):
        if not self._is_valid_number(a, b):
            return "Please enter numeric values only"
        result = a - b
        self._save_history(a, "-", b, result)
        return result

    def multiply(self, a, b):
        if not self._is_valid_number(a, b):
            return "Please enter numeric values only"
        result = a * b
        self._save_history(a, "*", b, result)
        return result

    def divide(self, a, b):
        if not self._is_valid_number(a, b):
            return "Please enter numeric values only"
        if b == 0:
            return "Cannot divide by zero"
        result = a / b
        self._save_history(a, "/", b, result)
        return result

    def power(self, a, b):
        if not self._is_valid_number(a, b):
            return "Please enter numeric values only"
        result = a ** b
        self._save_history(a, "**", b, result)
        return result

    def modulus(self, a, b):
        if not self._is_valid_number(a, b):
            return "Please enter numeric values only"
        if b == 0:
            return "Cannot find modulus with zero"
        result = a % b
        self._save_history(a, "%", b, result)
        return result

    def _save_history(self, a, operator, b, result):
        self._history.append(f"{a} {operator} {b} = {result}")

    def get_history(self):
        return list(self._history)

    def clear_history(self):
        self._history.clear()

    def _is_valid_number(self, a, b):
        return isinstance(a, (int, float)) and isinstance(b, (int, float))
