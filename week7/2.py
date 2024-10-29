class Process:
    def __init__(self, pid):
        self.pid = pid  # Process ID
        self.dependencies = set()  # Set of dependent process PIDs

    def add_dependency(self, process):
        """Add a process as a dependency."""
        self.dependencies.add(process.pid)

    def remove_dependency(self, process):
        """Remove a process from dependencies."""
        self.dependencies.discard(process.pid)

    def __str__(self):
        """String representation of the process and its dependencies."""
        return f"Process {self.pid} -> Dependencies: {list(self.dependencies)}"


class WaitForGraph:
    def __init__(self):
        self.processes = {}  # Stores processes by their PID

    def add_process(self, process):
        """Add a process to the wait-for graph."""
        self.processes[process.pid] = process

    def add_dependency(self, process_pid, dependency_pid):
        """Add a dependency between two processes."""
        if process_pid in self.processes and dependency_pid in self.processes:
            self.processes[process_pid].add_dependency(self.processes[dependency_pid])

    def remove_dependency(self, process_pid, dependency_pid):
        """Remove a dependency between two processes."""
        if process_pid in self.processes and dependency_pid in self.processes:
            self.processes[process_pid].remove_dependency(self.processes[dependency_pid])

    def detect_deadlocks(self):
        """Detect cycles in the wait-for graph (indicating deadlocks)."""
        visited = set()  # Tracks visited nodes
        recursion_stack = set()  # Tracks nodes in the current path (cycle detection)

        # Check for cycles starting from each process
        for process in self.processes.values():
            if self.detect_cycle(process, visited, recursion_stack):
                return True  # Deadlock detected
        return False  # No deadlock detected

    def detect_cycle(self, process, visited, recursion_stack):
        """Detect cycle using DFS."""
        if process.pid in recursion_stack:
            return True  # Cycle detected

        if process.pid in visited:
            return False  # Already visited, no cycle from here

        # Mark the current process as visited and add to recursion stack
        visited.add(process.pid)
        recursion_stack.add(process.pid)

        # Recursively check all dependencies for cycles
        for dep_pid in process.dependencies:
            dep_process = self.processes[dep_pid]
            if self.detect_cycle(dep_process, visited, recursion_stack):
                return True

        # Backtrack: Remove from recursion stack
        recursion_stack.remove(process.pid)
        return False

    def print_wfg(self):
        """Print the current state of the wait-for graph."""
        print("Wait-For Graph:")
        for process in self.processes.values():
            print(process)


# Driver Code
process1 = Process(1)
process2 = Process(2)
process3 = Process(3)
process4 = Process(4)

wfg = WaitForGraph()
wfg.add_process(process1)
wfg.add_process(process2)
wfg.add_process(process3)
wfg.add_process(process4)

wfg.add_dependency(1, 2)
wfg.add_dependency(2, 3)
wfg.add_dependency(3, 4)
wfg.add_dependency(4, 1)  # This creates a cycle (deadlock)

wfg.print_wfg()

if wfg.detect_deadlocks():
    print("Deadlock detected in the system.")
    wfg.remove_dependency(4, 1)  # Resolving deadlock by breaking the cycle
    print("Deadlock resolved.")
else:
    print("No deadlock detected.")

wfg.print_wfg()
