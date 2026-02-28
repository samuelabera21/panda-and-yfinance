class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def introduce(self):
        return f"Hi, I am {self.name} from grade {self.grade}."


def run_demo():
    print("CLASS & OBJECT DEMO")
    student = Student("Aarav", 10)
    print(student.introduce())
    print()
