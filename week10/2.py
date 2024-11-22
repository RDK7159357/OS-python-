from collections import deque

class LibraryShelf:
    def __init__(self, capacity):
        """
        Initialize the LibraryShelf with a given capacity.
        """
        self.capacity = capacity
        self.books = deque()  # Using deque to handle books efficiently

    def add_book(self, book):
        """
        Add a book to the shelf. If the shelf exceeds capacity,
        remove the oldest book.
        """
        if len(self.books) == self.capacity:
            removed_book = self.books.popleft()  # Remove the oldest book
            print(f"Removed book: {removed_book}")
        self.books.append(book)  # Add the new book

    def display_books(self):
        """
        Display the books currently on the shelf.
        """
        if not self.books:
            print("The shelf is empty.")
        else:
            print("Books on the shelf:")
            for book in self.books:
                print(f"- {book}")


# Driver Code
library_shelf = LibraryShelf(capacity=2)
books = [
    "The Great Adventure",
    "Mystery of the Lost City",
    "Journey Through Time",
   
]

for book in books:
    library_shelf.add_book(book)

library_shelf.display_books()
