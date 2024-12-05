class Process:
    def __init__(self, pid, arrival, burst):
        self.pid = pid
        self.arrival = arrival
        self.burst = burst
        self.remaining = burst
        self.waiting = 0
        self.turnaround = 0

def round_robin(processes, time_quantum):
    queue = sorted(processes, key=lambda p: p.arrival)  # Sort by arrival time
    current_time = 0
    while any(p.remaining > 0 for p in processes):  # Continue until all processes are completed
        for process in queue:
            if process.remaining > 0 and process.arrival <= current_time:
                time_used = min(process.remaining, time_quantum)
                process.remaining -= time_used
                current_time += time_used
                if process.remaining == 0:  # Process completed
                    process.turnaround = current_time - process.arrival
                    process.waiting = process.turnaround - process.burst
            elif process.arrival > current_time:
                current_time += 1  # Move time forward if no process is ready

def evaluate(processes):
    avg_wait = sum(p.waiting for p in processes) / len(processes)
    avg_tat = sum(p.turnaround for p in processes) / len(processes)
    print(f"Avg Waiting Time: {avg_wait:.2f}, Avg Turnaround Time: {avg_tat:.2f}")
    for p in processes:
        print(f"Process {p.pid}: Waiting = {p.waiting}, Turnaround = {p.turnaround}")

# Example Usage
if __name__ == "__main__":
    procs = [Process(1, 0, 8), Process(2, 1, 4), Process(3, 2, 9), Process(4, 3, 5)]
    round_robin(procs, time_quantum=2)
    evaluate(procs)
