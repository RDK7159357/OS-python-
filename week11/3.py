import threading
import time

# Semaphore to ensure only one employee uses the conference room at a time
conference_room_semaphore = threading.Semaphore(1)

def employee(name, start_time, end_time):
    """
    Simulates an employee using the conference room.
    :param name: Name of the employee
    :param start_time: Start time for the conference room
    :param end_time: End time for the conference room
    """
    # Log the request
    print(f"Employee {name} has requested the conference room from {start_time} to {end_time}.")
    
    # Wait for the conference room to become available
    with conference_room_semaphore:
        print(f"Employee {name} is now using the conference room from {start_time} to {end_time}.")
        
        # Simulate the time spent in the conference room
        duration = int(end_time.split(":")[0]) - int(start_time.split(":")[0])
        time.sleep(duration)  # Using hours as seconds for simplicity
        
        print(f"Employee {name} has finished using the conference room.")

# Driver Code
employee_threads = [
    threading.Thread(target=employee, args=("A", "10:00", "11:00")),
    threading.Thread(target=employee, args=("B", "11:00", "12:00")),
    threading.Thread(target=employee, args=("C", "12:00", "13:00"))
]

# Start all threads
for thread in employee_threads:
    thread.start()

# Wait for all threads to finish
for thread in employee_threads:
    thread.join()

print("All employees have finished using the conference room.")
