from basic_oop.demo import run_all_basic_oop_demos
from inheritance.demo import run_all_inheritance_demos
from library_system.demo import run_demo as run_library_system_demo
from real_app.demo import run_demo as run_real_app_demo


def main():
    run_all_basic_oop_demos()
    run_all_inheritance_demos()
    run_real_app_demo()
    run_library_system_demo()


if __name__ == "__main__":
    main()
