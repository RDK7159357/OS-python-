from collections import Counter
import heapq

class LibraryDisplay:
    def __init__(self, capacity):
        """
        Initialize the LibraryDisplay with a given capacity.
        """
        self.capacity = capacity
        self.books = []  # Min-heap to track the least popular books in the top display
        self.book_counts = Counter()  # To track the total times each book is checked out

    def add_book(self, book, times_checked_out):
        """
        Add a book to the display and update its checkout count.
        Maintain only the top books based on times checked out.
        """
        self.book_counts[book] += times_checked_out

        # Push the updated book to the heap
        heapq.heappush(self.books, (self.book_counts[book], book))

        # Remove excess books while keeping only the top ones
        while len(self.books) > self.capacity:
            heapq.heappop(self.books)

        # Rebuild the heap to ensure it only contains valid top books
        # We compare the stored heap with actual counts
        self.books = heapq.nlargest(self.capacity, [(self.book_counts[b], b) for _, b in self.books])
        heapq.heapify(self.books)

    def display_books(self):
        """
        Display the books currently in the library display, sorted by popularity.
        """
        if not self.books:
            print("The library display is empty.")
        else:
            print("Books on display (most checked out):")
            # Sort books by times checked out (descending) and then alphabetically
            display_list = sorted(self.books, key=lambda x: (-x[0], x[1]))
            for times, book in display_list:
                print(f"{book} - Checked out {times} times")


# Driver Code
library_display = LibraryDisplay(capacity=3)
book_checkouts = [
    ("The Great Gatsby", 3),
    ("1984", 5),
    ("To Kill a Mockingbird", 2),
    ("Pride and Prejudice", 4),
  
]

for book, times_checked_out in book_checkouts:
    library_display.add_book(book, times_checked_out)

library_display.display_books()
