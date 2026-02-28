from library_system.library_management import Book, Library, Member


def run_demo():
    print("=" * 50)
    print("REAL APP DEMO: LIBRARY SYSTEM")
    print("=" * 50)

    library = Library("City Library")

    library.add_book(Book(1, "Python Basics", "John Doe"))
    library.add_book(Book(2, "OOP in Action", "Jane Smith"))

    library.register_member(Member(101, "Aarav"))
    library.register_member(Member(102, "Riya"))

    print(library.issue_book(1, 101))
    print(library.issue_book(1, 102))
    print(library.return_book(1))
    print(library.available_books())
    print()
