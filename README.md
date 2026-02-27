# Basic Python Concepts: Array, Abstraction, and Polymorphism

This mini project explains three beginner-friendly OOP and data concepts in Python:

1. **Array (List) basics**
2. **Abstraction**
3. **Polymorphism**

---

## File

- `main.py` -> contains all examples

---

## What this code shows

### 1) Array (List) basics
In Python, we usually use a **list** as an array-like structure.

In `array_demo(numbers)`, you can see:
- create a list
- add item with `append`
- update item using index
- get length with `len`
- find total with `sum`
- calculate average

### 2) Abstraction
`Animal` is an **abstract class** (using `ABC`).

- It defines a method `speak()`
- It does not give actual sound
- Child classes must implement it

This hides the implementation details and gives a common interface.

### 3) Polymorphism
`Dog`, `Cat`, and `Cow` all implement `speak()` differently.

In `animal_sound_demo(animals)`, we loop through one list and call:

`animal.speak()`

Same method name, different output depending on object type. This is polymorphism.

---

## How to run

1. Open terminal in this folder
2. Run:

```bash
python main.py
```

If your system uses `python3`, run:

```bash
python3 main.py
```

---

## Example output

```text
ARRAY DEMO
Original list: [10, 20, 30]
After append(40): [10, 20, 30, 40]
After changing index 0 to 99: [99, 20, 30, 40]
Length: 4
Sum: 189
Average: 47.25

ABSTRACTION + POLYMORPHISM DEMO
Dog says Woof!
Cat says Meow!
Cow says Moo!
```
