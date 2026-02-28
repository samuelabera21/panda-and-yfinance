class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_issued = False


class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name


class Library:
    def __init__(self, name):
        self.name = name
        self.books = {}
        self.members = {}

    def add_book(self, book):
        self.books[book.book_id] = book

    def register_member(self, member):
        self.members[member.member_id] = member

    def issue_book(self, book_id, member_id):
        book = self.books.get(book_id)
        member = self.members.get(member_id)

        if not book:
            return "Book not found"
        if not member:
            return "Member not found"
        if book.is_issued:
            return f"Book '{book.title}' is already issued"

        book.is_issued = True
        return f"Book '{book.title}' issued to {member.name}"

    def return_book(self, book_id):
        book = self.books.get(book_id)
        if not book:
            return "Book not found"
        if not book.is_issued:
            return f"Book '{book.title}' was not issued"

        book.is_issued = False
        return f"Book '{book.title}' returned successfully"

    def available_books(self):
        available = [book for book in self.books.values() if not book.is_issued]
        if not available:
            return "No books available"
        lines = ["Available books:"]
        for book in available:
            lines.append(f"- {book.title} by {book.author}")
        return "\n".join(lines)
