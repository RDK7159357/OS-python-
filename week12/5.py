import threading
import time

# Define locks
locks = {"prop_x": threading.Lock(), "prop_y": threading.Lock()}

def rehearse(actor_name, need_prop_x, need_prop_y, rehearsal_time):
    resources = [
        (locks["prop_x"], "Prop X") if need_prop_x else None,
        (locks["prop_y"], "Prop Y") if need_prop_y else None,
    ]
    resources = [r for r in resources if r]

    print(f"{actor_name} waiting for resources...")
    for lock, res in resources:
        lock.acquire()
        print(f"{actor_name} reserved {res}.")

    print(f"{actor_name} rehearsing for {rehearsal_time} seconds...")
    time.sleep(rehearsal_time)

    for lock, res in resources:
        lock.release()
        print(f"{actor_name} released {res}.")

    print(f"{actor_name} completed rehearsal.")

# Driver Code
threads = [
    threading.Thread(target=rehearse, args=("E", True, True, 3)),
    threading.Thread(target=rehearse, args=("L", True, True, 2)),
]

[t.start() for t in threads]
[t.join() for t in threads]

print("All rehearsals have been completed.")
