class Dog:
    def speak(self):
        return "Woof!"


class Cat:
    def speak(self):
        return "Meow!"


class Cow:
    def speak(self):
        return "Moo!"


def run_demo():
    print("POLYMORPHISM DEMO")
    animals = [Dog(), Cat(), Cow()]
    for animal in animals:
        print(f"{type(animal).__name__} says {animal.speak()}")
    print()
