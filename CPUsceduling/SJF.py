class Process:
    def __init__(self, pid, arrival, burst):
        self.pid = pid
        self.arrival = arrival
        self.burst = burst
        self.waiting = 0
        self.turnaround = 0

def sjf(processes):
    current_time = 0
    for process in sorted(processes, key=lambda p: (p.arrival, p.burst)):
        if current_time < process.arrival:
            current_time = process.arrival
        process.waiting = current_time - process.arrival
        process.turnaround = process.waiting + process.burst
        current_time += process.burst


def evaluate(processes):
    avg_wait = sum(p.waiting for p in processes) / len(processes)
    avg_tat = sum(p.turnaround for p in processes) / len(processes)
    print(f"Avg Waiting Time: {avg_wait:.2f}, Avg Turnaround Time: {avg_tat:.2f}")
    for p in processes:
        print(f"Process {p.pid}: Waiting = {p.waiting}, Turnaround = {p.turnaround}")

# Example usage
if __name__ == "__main__":
    procs = [Process(1, 0, 8), Process(2, 1, 4), Process(3, 2, 9), Process(4, 3, 5)]
    sjf(procs)
    evaluate(procs)
