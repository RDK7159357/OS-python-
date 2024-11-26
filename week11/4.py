import threading
import time
from collections import deque

# Semaphore for stove and refrigerator to ensure one cook at a time
stove_semaphore = threading.Semaphore(1)
refrigerator_semaphore = threading.Semaphore(1)

# Queue to track requests
request_queue = deque()

# Lock to synchronize access to the request queue
queue_lock = threading.Lock()

def cook(name, stove_time, refrigerator_time):
    """
    Simulates a cook using the stove and refrigerator.
    :param name: Name of the cook
    :param stove_time: Time required to use the stove
    :param refrigerator_time: Time required to use the refrigerator
    """
    # Add the cook's request to the queue
    with queue_lock:
        request_queue.append((name, stove_time, refrigerator_time))
        print(f"Cook {name} has requested the stove for {stove_time} seconds and the refrigerator for {refrigerator_time} seconds.")

    # Wait for the stove to become available
    with stove_semaphore:
        # Simulate using the stove
        print(f"Cook {name} is now using the stove for {stove_time} seconds.")
        time.sleep(stove_time)
        print(f"Cook {name} has finished using the stove.")

    # Wait for the refrigerator to become available
    with refrigerator_semaphore:
        # Simulate using the refrigerator
        print(f"Cook {name} is now using the refrigerator for {refrigerator_time} seconds.")
        time.sleep(refrigerator_time)
        print(f"Cook {name} has finished using the refrigerator.")

# Driver Code
cook_threads = [
    threading.Thread(target=cook, args=("J", 2, 1)),
    threading.Thread(target=cook, args=("M", 3, 2)),
    threading.Thread(target=cook, args=("R", 1, 1))
]

# Start all threads
for thread in cook_threads:
    thread.start()

# Wait for all threads to finish
for thread in cook_threads:
    thread.join()

print("All cooks have finished using the stove and refrigerator.")
