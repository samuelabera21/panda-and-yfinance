from inheritance.single_inheritance import run_demo as single_inheritance_demo
from inheritance.multilevel_inheritance import run_demo as multilevel_inheritance_demo
from inheritance.hierarchical_inheritance import run_demo as hierarchical_inheritance_demo


def run_all_inheritance_demos():
    print("=" * 50)
    print("INHERITANCE CONCEPTS")
    print("=" * 50)
    single_inheritance_demo()
    multilevel_inheritance_demo()
    hierarchical_inheritance_demo()
