import threading
import time

# Define locks
locks = {"espresso_machine": threading.Lock(), "blender": threading.Lock()}

def make_drink(barista_name, need_espresso_machine, need_blender, work_time):
    resources = [
        (locks["espresso_machine"], "Espresso Machine") if need_espresso_machine else None,
        (locks["blender"], "Blender") if need_blender else None,
    ]
    resources = [r for r in resources if r]  # Filter required resources

    print(f"{barista_name} waiting for resources...")
    for lock, res in resources:
        lock.acquire()
        print(f"{barista_name} reserved {res}.")

    print(f"{barista_name} preparing drink for {work_time} seconds...")
    time.sleep(work_time)

    for lock, res in resources:
        lock.release()
        print(f"{barista_name} released {res}.")

    print(f"{barista_name} finished preparing the drink.")

# Driver Code
threads = [
    threading.Thread(target=make_drink, args=("Anna", True, True, 3)),
    threading.Thread(target=make_drink, args=("Ben", True, True, 2)),
]

for t in threads:
    t.start()
for t in threads:
    t.join()

print("All drinks have been prepared.")
