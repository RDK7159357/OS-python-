import threading
import time

# Define resource locks
locks = {
    "robot_a": threading.Lock(),
    "robot_b": threading.Lock(),
    "bin_1": threading.Lock(),
    "bin_2": threading.Lock(),
}

def task(name, need_robot_a, need_robot_b, need_bin_1, need_bin_2, work_time):
    resources = [
        (locks["robot_a"], "Robot A") if need_robot_a else None,
        (locks["robot_b"], "Robot B") if need_robot_b else None,
        (locks["bin_1"], "Bin 1") if need_bin_1 else None,
        (locks["bin_2"], "Bin 2") if need_bin_2 else None,
    ]
    resources = [r for r in resources if r]  # Filter required locks

    print(f"Task {name} waiting for resources...")
    for lock, res in resources:
        lock.acquire()
        print(f"Task {name} reserved {res}.")

    print(f"Task {name} working for {work_time} seconds...")
    time.sleep(work_time)

    for lock, res in resources:
        lock.release()
        print(f"Task {name} released {res}.")

    print(f"Task {name} completed.")

# Driver Code
threads = [
    threading.Thread(target=task, args=("A", True, True, True, True, 3)),
    threading.Thread(target=task, args=("B", True, True, True, True, 2)),
]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print("All tasks have been completed.")
