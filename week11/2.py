import threading
import time

# Semaphore for each machine to ensure mutual exclusion
machine_1_semaphore = threading.Semaphore(1)
machine_2_semaphore = threading.Semaphore(1)

def barista(name, machine, preparation_time):
    """
    Represents a barista trying to use a coffee machine.
    :param name: Name of the barista
    :param machine: The machine they want to use ("Machine 1" or "Machine 2")
    :param preparation_time: Time required for preparation
    """
    # Select the correct semaphore for the machine
    semaphore = machine_1_semaphore if machine == "Machine 1" else machine_2_semaphore

    # Request to use the machine
    print(f"{name} has requested {machine} for {preparation_time} seconds.")

    # Wait for the semaphore to become available
    with semaphore:
        print(f"{name} is now using {machine} for {preparation_time} seconds.")
        
        # Simulate the preparation time
        time.sleep(preparation_time)
        
        print(f"{name} has finished using {machine}.")

# Driver Code
barista_threads = [
    threading.Thread(target=barista, args=("Emma", "Machine 1", 2)),
    threading.Thread(target=barista, args=("Liam", "Machine 2", 3)),
    threading.Thread(target=barista, args=("Olivia", "Machine 1", 1))
]

# Start all threads
for thread in barista_threads:
    thread.start()

# Wait for all threads to finish
for thread in barista_threads:
    thread.join()

print("All baristas have finished using the coffee machines.")
