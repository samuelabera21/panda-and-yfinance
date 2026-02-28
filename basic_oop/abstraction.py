from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


def run_demo():
    print("ABSTRACTION DEMO")
    rectangle = Rectangle(5, 4)
    print(f"Rectangle area: {rectangle.area()}")
    print()
