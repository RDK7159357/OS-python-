class BestFitMemoryManager:
    def __init__(self, memory_blocks):
        self.memory_blocks = memory_blocks
        self.available_blocks = {i: block for i, block in enumerate(memory_blocks)}
        self.processes = {}

    def allocate_memory(self, process_id, size):
        best_fit = None
        for partition_id, partition_size in self.available_blocks.items():
            if partition_size >= size:
                if best_fit is None or partition_size < self.available_blocks[best_fit]:
                    best_fit = partition_id

        if best_fit is not None:
            self.available_blocks[best_fit] -= size
            self.processes[process_id] = (best_fit, size)
            print(f"Process {process_id} allocated {size} KB in Partition {best_fit}")
            return True
        else:
            print(f"Process {process_id} allocation of {size} KB failed")
            return False

    def deallocate_memory(self, process_id):
        if process_id in self.processes:
            partition_id, size = self.processes.pop(process_id)
            self.available_blocks[partition_id] += size
            print(f"Process {process_id} deallocated from Partition {partition_id}")
        else:
            print(f"Process {process_id} not found")

    def display_memory_status(self):
        print("Current Memory Allocation Status:")
        for partition_id, partition_size in self.available_blocks.items():
            print(f"Partition {partition_id}: {partition_size} KB available")

# Driver Code
memory_manager = BestFitMemoryManager([100, 200, 50, 150, 300, 80, 120, 200])
memory_manager.allocate_memory(1, 70)
memory_manager.allocate_memory(2, 180)
memory_manager.allocate_memory(3, 250)
memory_manager.display_memory_status()
memory_manager.deallocate_memory(2)
print("\nAfter deallocating Process 2:")
memory_manager.display_memory_status()
