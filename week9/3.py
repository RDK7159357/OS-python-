import threading
import time
import random

class InventorySystem:
    def __init__(self):
        # Initial inventory with some items and quantities
        self.inventory = {'item1': 100, 'item2': 100, 'item3': 100}
        self.lock = threading.Lock()  # Lock to handle concurrent access

    def add_item(self, item, quantity):
        # Safely add items to the inventory
        with self.lock:
            if item in self.inventory:
                self.inventory[item] += quantity
            else:
                self.inventory[item] = quantity
            print(f"Added {quantity} of {item}. New stock: {self.inventory[item]}")

    def remove_item(self, item, quantity):
        # Safely remove items from the inventory
        with self.lock:
            if item in self.inventory and self.inventory[item] >= quantity:
                self.inventory[item] -= quantity
                print(f"Removed {quantity} of {item}. New stock: {self.inventory[item]}")
                return True  # Indicate that the removal was successful
            else:
                print(f"Failed to remove {quantity} of {item}. Insufficient stock.")
                return False  # Indicate that the removal failed


class ShoppingCart:
    def __init__(self):
        # Dictionary to hold each user's cart items
        self.carts = {}
        self.lock = threading.Lock()  # Lock to handle concurrent access

    def add_to_cart(self, user_id, item, quantity):
        with self.lock:
            if user_id not in self.carts:
                self.carts[user_id] = {}
            if item in self.carts[user_id]:
                self.carts[user_id][item] += quantity
            else:
                self.carts[user_id][item] = quantity
            print(f"{user_id} added {quantity} of {item} to their cart.")

    def remove_from_cart(self, user_id, item, quantity):
        with self.lock:
            if user_id in self.carts and item in self.carts[user_id] and self.carts[user_id][item] >= quantity:
                self.carts[user_id][item] -= quantity
                if self.carts[user_id][item] == 0:
                    del self.carts[user_id][item]
                print(f"{user_id} removed {quantity} of {item} from their cart.")
                return True
            else:
                print(f"{user_id} failed to remove {quantity} of {item} from their cart.")
                return False


def customer_action(user_id, cart, inventory):
    # Randomly decide to add or remove items from cart
    actions = ['add', 'remove']
    items = list(inventory.inventory.keys())
    
    for _ in range(5):  # Each user performs 5 actions
        action = random.choice(actions)
        item = random.choice(items)
        quantity = random.randint(1, 5)
        
        if action == 'add':
            if inventory.remove_item(item, quantity):  # Check if enough inventory exists to add
                cart.add_to_cart(user_id, item, quantity)
        elif action == 'remove':
            if cart.remove_from_cart(user_id, item, quantity):
                inventory.add_item(item, quantity)  # Return item to inventory if successfully removed from cart

        time.sleep(random.uniform(0.1, 0.5))  # Simulate time delay between actions


# Driver Code
inventory = InventorySystem()
cart = ShoppingCart()
threads = []
user_ids = [f'User{i+1}' for i in range(10)]

for user_id in user_ids:
    for _ in range(5):  # Each user has 5 threads for actions
        t = threading.Thread(target=customer_action, args=(user_id, cart, inventory))
        threads.append(t)
        t.start()

for t in threads:
    t.join()

print("All customer actions completed.")
