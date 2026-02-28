from real_app.grading_system import GradeBook, Student


def run_demo():
    print("=" * 50)
    print("REAL APP DEMO: GRADING SYSTEM")
    print("=" * 50)

    gradebook = GradeBook("Class 10")

    students = [
        Student("Aarav", 1),
        Student("Riya", 2),
        Student("Kabir", 3),
    ]

    for student in students:
        gradebook.add_student(student)

    gradebook.add_score(1, 95)
    gradebook.add_score(1, 89)
    gradebook.add_score(2, 78)
    gradebook.add_score(2, 84)
    gradebook.add_score(3, 65)
    gradebook.add_score(3, 72)

    print(gradebook.class_report())
    print()
