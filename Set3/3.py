# 9. Disk Scheduling using FCFS
def disk_scheduling_fcfs(requests, head):
    print(f"Initial Head Position: {head}")
    for request in requests:
        print(f"Moving from {head} to {request}")
        head = request

requests = [82, 170, 43, 140, 24, 16, 190]
initial_head = 50
disk_scheduling_fcfs(requests, initial_head)