class Process:
    def __init__(self, pid, max_resources):
        self.pid = pid  # Process ID
        self.max_resources = max_resources  # Maximum resources the process can use
        self.allocated_resources = {resource: 0 for resource in max_resources}  # Currently allocated resources

    def request_resource(self, resource, amount):
        """Request a specific amount of resource."""
        if resource not in self.max_resources:
            return False  # Resource not available for this process

        # Ensure the request doesn't exceed the maximum limit of the process
        if self.allocated_resources[resource] + amount > self.max_resources[resource]:
            return False

        self.allocated_resources[resource] += amount
        return True

    def release_resource(self, resource, amount):
        """Release a specific amount of resource."""
        if resource not in self.allocated_resources:
            return False  # Resource not allocated to this process

        # Ensure the process cannot release more than it currently holds
        if self.allocated_resources[resource] < amount:
            return False

        self.allocated_resources[resource] -= amount
        return True

    def __str__(self):
        """String representation of the process status."""
        return f"Process {self.pid} - Allocated: {self.allocated_resources}"


class ResourceManager:
    def __init__(self, resources):
        self.total_resources = resources  # Total available resources in the system
        self.available_resources = resources.copy()  # Track available resources
        self.processes = {}  # Store processes by their PID

    def add_process(self, process):
        """Add a process to the manager."""
        self.processes[process.pid] = process

    def request_resource(self, process_id, resource, amount):
        """Handle a resource request from a process."""
        if process_id not in self.processes:
            return False  # Process not found

        if resource not in self.available_resources:
            return False  # Resource not managed

        # Check if there are enough available resources
        if self.available_resources[resource] < amount:
            return False

        # Delegate the request to the process
        process = self.processes[process_id]
        if process.request_resource(resource, amount):
            self.available_resources[resource] -= amount  # Update available resources
            return True
        return False

    def release_resource(self, process_id, resource, amount):
        """Handle a resource release from a process."""
        if process_id not in self.processes:
            return False  # Process not found

        if resource not in self.available_resources:
            return False  # Resource not managed

        # Delegate the release to the process
        process = self.processes[process_id]
        if process.release_resource(resource, amount):
            self.available_resources[resource] += amount  # Update available resources
            return True
        return False

    def print_processes_status(self):
        """Print the status of all processes and available resources."""
        print("Available Resources:", self.available_resources)
        for process in self.processes.values():
            print(process)


# Driver Code
resources = {"CPU": 1, "Memory": 1024}
process1 = Process(1, {"CPU": 1, "Memory": 512})
process2 = Process(2, {"CPU": 1, "Memory": 768})

resource_manager = ResourceManager(resources)
resource_manager.add_process(process1)
resource_manager.add_process(process2)

print("Initial State:")
resource_manager.print_processes_status()

if resource_manager.request_resource(1, "CPU", 1):
    print("Process 1 allocated CPU")
else:
    print("Process 1 failed to allocate CPU")

if resource_manager.request_resource(1, "Memory", 512):
    print("Process 1 allocated Memory")
else:
    print("Process 1 failed to allocate Memory")

resource_manager.print_processes_status()

if resource_manager.request_resource(2, "Memory", 768):
    print("Process 2 allocated Memory")
else:
    print("Process 2 failed to allocate Memory")

resource_manager.print_processes_status()

if resource_manager.release_resource(1, "Memory", 512):
    print("Process 1 released Memory")
else:
    print("Process 1 failed to release Memory")

resource_manager.print_processes_status()
