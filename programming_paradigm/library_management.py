# library_management.py

class Book:
    def __init__(self, title, author):
        """Initialize a book with title, author, and availability."""
        self.title = title
        self.author = author
        self._is_checked_out = False  # private attribute for availability

    def check_out(self):
        """Mark the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Mark the book as returned (available)."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Return True if the book is available, False if checked out."""
        return not self._is_checked_out

class Library:
    def __init__(self):
        """Initialize the library with a private list of books."""
        self._books = []

    def add_book(self, book):
        """Add a Book instance to the library collection."""
        if isinstance(book, Book):
            self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by title if it exists and is available."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return True
        return False

    def return_book(self, title):
        """Return a book by title if it exists and is checked out."""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return True
        return False

    def list_available_books(self):
        """Print all books that are currently available."""
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")
