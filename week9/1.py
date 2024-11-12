import threading
import time
import random

class BookInventory:
    def __init__(self):
        # Initialize the inventory with some books and their quantities
        self.inventory = {
            'Book1': 3,
            'Book2': 2,
            'Book3': 1
        }
        # Lock to handle concurrent access to the inventory
        self.lock = threading.Lock()
    
    def checkout_book(self, book):
        with self.lock:
            if self.inventory.get(book, 0) > 0:
                self.inventory[book] -= 1
                print(f"{book} checked out successfully. Remaining: {self.inventory[book]}")
            else:
                print(f"{book} is out of stock.")

    def return_book(self, book):
        with self.lock:
            self.inventory[book] = self.inventory.get(book, 0) + 1
            print(f"{book} returned successfully. Available now: {self.inventory[book]}")

def user_request(inventory, book, action):
    if action == 'checkout':
        inventory.checkout_book(book)
    elif action == 'return':
        inventory.return_book(book)
    else:
        print("Invalid action.")

# Driver Code
inventory = BookInventory()
threads = []
books = ['Book1', 'Book2', 'Book3']
actions = ['checkout', 'return']

for i in range(10):
    book = random.choice(books)
    action = random.choice(actions)
    t = threading.Thread(target=user_request, args=(inventory, book, action))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("All operations completed.")
