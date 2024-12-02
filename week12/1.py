import threading
import time

# Define the locks
locks = {
    "press_1": threading.Lock(),
    "press_2": threading.Lock(),
    "ink_a": threading.Lock(),
    "ink_b": threading.Lock(),
}

def use_resources(printer_name, need_press_1, need_press_2, need_ink_a, need_ink_b):
    required_locks = [
        locks["press_1"] if need_press_1 else None,
        locks["press_2"] if need_press_2 else None,
        locks["ink_a"] if need_ink_a else None,
        locks["ink_b"] if need_ink_b else None,
    ]
    required_locks = [lock for lock in required_locks if lock]  # Filter out unused locks

    print(f"Printer {printer_name} is waiting for resources...")
    for lock in required_locks:
        lock.acquire()
        print(f"Printer {printer_name} acquired {lock}.")

    print(f"Printer {printer_name} is using resources...")
    time.sleep(2)

    for lock in required_locks:
        lock.release()
        print(f"Printer {printer_name} released {lock}.")

    print(f"Printer {printer_name} completed its job.")

# Driver Code
threads = [
    threading.Thread(target=use_resources, args=("E", True, True, True, True)),
    threading.Thread(target=use_resources, args=("L", True, True, True, True)),
]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print("All jobs have been completed.")
