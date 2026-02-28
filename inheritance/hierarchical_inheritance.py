class Employee:
    def company(self):
        return "I work at ABC Pvt Ltd"


class Developer(Employee):
    def role(self):
        return "I build software"


class Designer(Employee):
    def role(self):
        return "I design user interfaces"


def run_demo():
    print("HIERARCHICAL INHERITANCE DEMO")
    developer = Developer()
    designer = Designer()
    print(developer.company())
    print(f"Developer: {developer.role()}")
    print(f"Designer: {designer.role()}")
    print()
