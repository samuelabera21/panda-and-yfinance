class Person:
    def info(self):
        return "I am a person"


class Teacher(Person):
    def teach(self):
        return "I teach students"


class MathTeacher(Teacher):
    def subject(self):
        return "I teach Mathematics"


def run_demo():
    print("MULTILEVEL INHERITANCE DEMO")
    math_teacher = MathTeacher()
    print(math_teacher.info())
    print(math_teacher.teach())
    print(math_teacher.subject())
    print()
