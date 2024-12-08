# 4. Software Developer Task using SJF Algorithm
def sjf(tasks):
    tasks.sort(key=lambda x: x['duration'])
    time = 0
    for task in tasks:
        print(f"Executing Task {task['id']} (Duration: {task['duration']}s) at t={time}s")
        time += task['duration']

jobs = [{'id': 1, 'duration': 6}, {'id': 2, 'duration': 8}, {'id': 3, 'duration': 7}, {'id': 4, 'duration': 3}]
sjf(jobs)