class Person:
    def __init__(self, name):
        self.name = name


class Student(Person):
    def __init__(self, name, roll_number):
        super().__init__(name)
        self.roll_number = roll_number


class GradeBook:
    def __init__(self, class_name):
        self.class_name = class_name
        self._students = {}
        self._scores = {}

    def add_student(self, student):
        self._students[student.roll_number] = student
        self._scores[student.roll_number] = []

    def add_score(self, roll_number, score):
        if roll_number in self._scores and 0 <= score <= 100:
            self._scores[roll_number].append(score)

    def average_score(self, roll_number):
        scores = self._scores.get(roll_number, [])
        if not scores:
            return 0
        return round(sum(scores) / len(scores), 2)

    def grade(self, average):
        if average >= 90:
            return "A"
        if average >= 80:
            return "B"
        if average >= 70:
            return "C"
        if average >= 60:
            return "D"
        return "F"

    def student_report(self, roll_number):
        student = self._students.get(roll_number)
        if not student:
            return "Student not found"

        avg = self.average_score(roll_number)
        letter = self.grade(avg)
        return (
            f"Name: {student.name}, Roll: {student.roll_number}, "
            f"Average: {avg}, Grade: {letter}"
        )

    def class_report(self):
        report_lines = [f"Class: {self.class_name}"]
        for roll_number in sorted(self._students):
            report_lines.append(self.student_report(roll_number))
        return "\n".join(report_lines)
