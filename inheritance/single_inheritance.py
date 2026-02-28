class Vehicle:
    def start(self):
        return "Vehicle started"


class Car(Vehicle):
    def honk(self):
        return "Car says beep beep"


def run_demo():
    print("SINGLE INHERITANCE DEMO")
    car = Car()
    print(car.start())
    print(car.honk())
    print()
