# 1. Busy Printer using FCFS Algorithm
def fcfs(printer_queue):
    time = 0
    for job in printer_queue:
        print(f"Processing job {job['id']} (Duration: {job['duration']}s) at t={time}s")
        time += job['duration']

jobs = [{'id': 1, 'duration': 5}, {'id': 2, 'duration': 3}, {'id': 3, 'duration': 2}]
fcfs(jobs)