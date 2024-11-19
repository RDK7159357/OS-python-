from collections import deque

class CafeFIFO:
    def __init__(self, capacity):
        """
        Initialize the CafeFIFO with a fixed capacity.
        """
        self.capacity = capacity  # Maximum number of orders the cafe can handle at a time
        self.orders = deque()     # Queue to store the orders

    def add_order(self, order):
        """
        Add a new order to the queue. If the queue is full, remove the oldest order.
        """
        if len(self.orders) >= self.capacity:
            removed_order = self.orders.popleft()  # Remove the oldest order
            print(f"Removed order: {removed_order}")
        self.orders.append(order)  # Add the new order
        print(f"Added order: {order}")

    def display_orders(self):
        """
        Display all the current orders in the queue.
        """
        print("Current orders in the queue:")
        for order in self.orders:
            print(order)

# Driver Code
cafe = CafeFIFO(capacity=4)
orders = ["Coffee", "Tea", "Muffin", "Croissant", "Smoothie"]

for order in orders:
    cafe.add_order(order)
    cafe.display_orders()
