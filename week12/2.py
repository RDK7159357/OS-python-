import threading
import time

# Define locks for resources
locks = {"book_a": threading.Lock(), "book_b": threading.Lock(), "desk": threading.Lock()}

def reserve_resources(reader_name, need_book_a, need_book_b, need_desk, reading_time):
    resources = [
        (locks["book_a"], "Book A") if need_book_a else None,
        (locks["book_b"], "Book B") if need_book_b else None,
        (locks["desk"], "Desk") if need_desk else None,
    ]
    resources = [r for r in resources if r]  # Filter resources

    print(f"{reader_name} waiting for resources...")
    for lock, res in resources:
        lock.acquire()
        print(f"{reader_name} reserved {res}.")

    print(f"{reader_name} is reading for {reading_time} seconds...")
    time.sleep(reading_time)

    for lock, res in resources:
        lock.release()
        print(f"{reader_name} released {res}.")

    print(f"{reader_name} completed reading.")

# Driver code
threads = [
    threading.Thread(target=reserve_resources, args=("Sophia", True, False, True, 2)),
    threading.Thread(target=reserve_resources, args=("Ethan", False, True, True, 1.5)),
]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print("All reservations have been completed.")
