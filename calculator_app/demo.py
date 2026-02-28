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

    print("History:")
    for item in calculator.get_history():
        print(f"- {item}")
    print()
