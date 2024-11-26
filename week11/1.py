import threading
import time
from queue import Queue

# Semaphore to represent the oven (1 at a time)
oven_semaphore = threading.Semaphore(1)

def baker(name, bake_time):
    """
    Represents a baker trying to use the oven.
    :param name: Name of the baker
    :param bake_time: Time required to bake
    """
    print(f"Baker {name} is waiting to use the oven.")
    
    # Attempt to acquire the semaphore (oven access)
    with oven_semaphore:
        print(f"Baker {name} has started using the oven.")
        time.sleep(bake_time)  # Simulate baking time
        print(f"Baker {name} has finished using the oven.")

# Driver Code
baker_threads = [
    threading.Thread(target=baker, args=("A", 2)),
    threading.Thread(target=baker, args=("B", 3)),
    threading.Thread(target=baker, args=("C", 1))
]

# Start all threads
for thread in baker_threads:
    thread.start()

# Wait for all threads to finish
for thread in baker_threads:
    thread.join()

print("All bakers have finished using the oven.")
