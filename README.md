# Python OOP Beginner Guide

This project is now organized into separate folders so beginners can learn object-oriented programming step by step.

## Project structure

- `main.py` -> runs all demos
- `basic_oop/` -> basic OOP concepts
	- `class_and_object.py`
	- `encapsulation.py`
	- `abstraction.py`
	- `polymorphism.py`
	- `demo.py`
- `inheritance/` -> inheritance-focused examples
	- `single_inheritance.py`
	- `multilevel_inheritance.py`
	- `hierarchical_inheritance.py`
	- `demo.py`
- `real_app/` -> real-world OOP mini app
	- `grading_system.py`
	- `demo.py`
- `library_system/` -> second real-world beginner project
	- `library_management.py`
	- `demo.py`

## Concepts covered

### Basic OOP
1. Class and object
2. Encapsulation
3. Abstraction
4. Polymorphism

### Inheritance
1. Single inheritance
2. Multilevel inheritance
3. Hierarchical inheritance

### Real app example
1. Student grading system using classes and objects
2. Encapsulation with internal student/score storage
3. Inheritance with `Student` extending `Person`
4. Practical methods: add students, add scores, generate reports

### Real app project 2
1. Library management system using `Book`, `Member`, and `Library` classes
2. Practical methods: add books, register members, issue and return books
3. State handling with `is_issued` for each book
4. Useful output for beginner understanding

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

## Learning tip

Start with files inside `basic_oop/` first, then continue to `inheritance/`.
Then open `real_app/grading_system.py` to see how OOP is used in a practical app.
After that, open `library_system/library_management.py` for another simple real-world project.
Each file contains a small runnable example and `main.py` runs everything together.
