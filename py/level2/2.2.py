class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"'{self.title}' by {self.author} ({self.year})"


class Reader:
    def __init__(self, name):
        self.name = name
        self.books = []

    def borrow_book(self, book, library):
        if library.lend_book(book, self):
            self.books.append(book)
            print(f"{self.name} borrowed {book}.")
        else:
            print(f"Sorry, {self.name}, the book {book} is not available.")

    def return_book(self, book, library):
        if book in self.books:
            self.books.remove(book)
            library.add_book(book)
            print(f"{self.name} returned {book}.")
        else:
            print(f"{self.name} doesn't have {book}.")

    def __str__(self):
        return f"Reader: {self.name}"


class Library:
    def __init__(self):
        self.books = []
        self.readers = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added {book} to the library.")

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f"Removed {book} from the library.")
        else:
            print(f"{book} not found in the library.")

    def lend_book(self, book, reader):
        if not book in self.books:
            return False
        self.books.remove(book)
        return True

    def register_reader(self, reader):
        self.readers.append(reader)
        print(f"Registered {reader} in the library.")

    def find_book(self, title):
        for book in self.books:
            if book.title == title: return book
        return None

    def __str__(self):
        return f"Library with {len(self.books)} books and {len(self.readers)} readers."

library = Library()

book1 = Book("To Kill a Mockingbird", "Harper Lee", 1960)
book2 = Book("1984", "George Orwell", 1949)
library.add_book(book1)
library.add_book(book2)

reader = Reader("Alice")
library.register_reader(reader)

reader.borrow_book(book1, library)
reader.return_book(book1, library)
reader.borrow_book(book1, library)