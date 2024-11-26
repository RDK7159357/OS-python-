import threading
import time

# Semaphore to ensure mutual exclusion for the water pump
water_pump_semaphore = threading.Semaphore(1)

def gardener(name, water_time):
    """
    Simulates a gardener using the water pump.
    :param name: Name of the gardener
    :param water_time: Time required to use the water pump (in seconds)
    """
    print(f"Gardener {name} has requested the water pump for {water_time} seconds.")
    
    # Wait for the water pump to become available
    with water_pump_semaphore:
        print(f"Gardener {name} is now using the water pump for {water_time} seconds.")
        
        # Simulate watering time
        time.sleep(water_time)
        
        print(f"Gardener {name} has finished using the water pump.")

# Driver Code
gardener_threads = [
    threading.Thread(target=gardener, args=("Sophia", 30)),
    threading.Thread(target=gardener, args=("James", 45)),
    threading.Thread(target=gardener, args=("Oliver", 20))
]

# Start all threads
for thread in gardener_threads:
    thread.start()

# Wait for all threads to finish
for thread in gardener_threads:
    thread.join()

print("All gardeners have finished using the water pump.")
