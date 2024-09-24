class MFTMemoryManager:
    def __init__(self, num_partitions, partition_size):
        self.num_partitions = num_partitions
        self.partition_size = partition_size
        self.available_partitions = [True] * num_partitions
        self.processes = {}

    def allocate_memory(self, process_id, size):
        if size > self.partition_size:
            print(f"Process {process_id} requires more memory than a single partition can provide.")
            return False
        for i in range(self.num_partitions):
            if self.available_partitions[i]:
                self.available_partitions[i] = False
                self.processes[process_id] = i
                print(f"Allocated partition {i} to process {process_id}.")
                return True
        print(f"No available partition for process {process_id}.")
        return False

    def deallocate_memory(self, process_id):
        if process_id in self.processes:
            partition_index = self.processes.pop(process_id)
            self.available_partitions[partition_index] = True
            print(f"Deallocated partition {partition_index} from process {process_id}.")
        else:
            print(f"Process {process_id} not found.")

    def display_memory_status(self):
        print("Memory Status:")
        for i in range(self.num_partitions):
            status = "Free" if self.available_partitions[i] else "Occupied"
            print(f"Partition {i}: {status}")

# Driver Code
memory_manager = MFTMemoryManager(num_partitions=8, partition_size=800)
memory_manager.allocate_memory(1, 600)
memory_manager.allocate_memory(2, 900)
memory_manager.allocate_memory(3, 400)
memory_manager.display_memory_status()
memory_manager.deallocate_memory(2)
print("\nAfter deallocating Process 2:")
memory_manager.display_memory_status()
