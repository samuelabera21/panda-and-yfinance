from calculator_app.calculator import Calculator


def run_demo():
    print("=" * 50)
    print("REAL APP DEMO: CALCULATOR")
    print("=" * 50)

    calculator = Calculator()

    print(f"10 + 5 = {calculator.add(10, 5)}")
    print(f"10 - 5 = {calculator.subtract(10, 5)}")
    print(f"10 * 5 = {calculator.multiply(10, 5)}")
    print(f"10 / 5 = {calculator.divide(10, 5)}")
    print(f"10 / 0 = {calculator.divide(10, 0)}")
    print(f"2 ** 4 = {calculator.power(2, 4)}")
    print(f"10 % 3 = {calculator.modulus(10, 3)}")
    print(f"'a' + 5 = {calculator.add('a', 5)}")

    print("History:")
    for item in calculator.get_history():
        print(f"- {item}")

    calculator.clear_history()
    print(f"History cleared. Total records: {len(calculator.get_history())}")
    print()
