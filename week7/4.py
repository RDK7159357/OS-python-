import threading
import time
import random

class Philosopher(threading.Thread):
    def __init__(self, philosopher_id, left_utensil, right_utensil):
        super().__init__()
        self.philosopher_id = philosopher_id
        self.left_utensil = left_utensil
        self.right_utensil = right_utensil

    def run(self):
        """Philosopher's lifecycle: thinking and eating."""
        while True:
            self.think()
            self.eat()

    def think(self):
        """Simulate thinking."""
        print(f"Philosopher {self.philosopher_id} is thinking...")
        time.sleep(random.uniform(1, 3))  # Thinking for some time

    def eat(self):
        """Attempt to eat by acquiring both utensils."""
        # Try to acquire the left and right utensils
        left_acquired = self.left_utensil.acquire(timeout=1)
        if left_acquired:
            right_acquired = self.right_utensil.acquire(timeout=1)

            if right_acquired:
                # If both utensils are acquired, eat
                print(f"Philosopher {self.philosopher_id} is eating...")
                time.sleep(random.uniform(1, 2))  # Eating for some time
                self.right_utensil.release()  # Release right utensil
            else:
                # If right utensil is not acquired, release the left utensil
                print(f"Philosopher {self.philosopher_id} couldn't acquire both utensils.")
            
            self.left_utensil.release()  # Release left utensil

# Driver Code
num_philosophers = 5

# Create one lock (utensil) for each philosopher
utensils = [threading.Lock() for _ in range(num_philosophers)]

# Create and start the philosopher threads
philosophers = []
for i in range(num_philosophers):
    left_utensil = utensils[i]
    right_utensil = utensils[(i + 1) % num_philosophers]  # Circular arrangement
    philosopher = Philosopher(i + 1, left_utensil, right_utensil)
    philosophers.append(philosopher)

# Start all philosopher threads
for philosopher in philosophers:
    philosopher.start()
