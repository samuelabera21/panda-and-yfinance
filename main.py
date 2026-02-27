from abc import ABC, abstractmethod


# ----------------------
# 1) Array (List) Example
# ----------------------
def array_demo(numbers):
    """Shows basic array/list operations."""
    print("ARRAY DEMO")
    print("Original list:", numbers)

    numbers.append(40)            # add a value
    print("After append(40):", numbers)

    numbers[0] = 99               # update by index
    print("After changing index 0 to 99:", numbers)

    print("Length:", len(numbers))
    print("Sum:", sum(numbers))
    print("Average:", sum(numbers) / len(numbers))
    print()


# ----------------------
# 2) Abstraction + Polymorphism Example
# ----------------------
class Animal(ABC):
    """Abstract base class (abstraction)."""

    @abstractmethod
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


class Cow(Animal):
    def speak(self):
        return "Moo!"


def animal_sound_demo(animals):
    """Polymorphism: same method call, different behavior."""
    print("ABSTRACTION + POLYMORPHISM DEMO")
    for animal in animals:  # array/list of Animal objects
        print(type(animal).__name__, "says", animal.speak())


if __name__ == "__main__":
    # Array demo with integers
    values = [10, 20, 30]
    array_demo(values)

    # Polymorphism demo with different Animal objects in one list
    pet_list = [Dog(), Cat(), Cow()]
    animal_sound_demo(pet_list)
