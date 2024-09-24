class WorstFitMemoryManager:
    def __init__(self, memory_blocks):
        self.memory_blocks = memory_blocks
        self.available_blocks = {i: block for i, block in enumerate(memory_blocks)}
        self.processes = {}

    def allocate_memory(self, process_id, size):
        # Find the worst fit block (largest block that can fit the process)
        worst_fit_index = -1
        max_size = -1
        for index, block_size in self.available_blocks.items():
            if block_size >= size and block_size > max_size:
                worst_fit_index = index
                max_size = block_size

        if worst_fit_index == -1:
            print(f"Process {process_id} allocation of {size} KB failed")
            return False

        # Allocate memory
        self.available_blocks[worst_fit_index] -= size
        if self.available_blocks[worst_fit_index] == 0:
            del self.available_blocks[worst_fit_index]
        self.processes[process_id] = (worst_fit_index, size)
        print(f"Process {process_id} allocated {size} KB in Block {worst_fit_index}")
        return True

    def deallocate_memory(self, process_id):
        if process_id in self.processes:
            block_index, size = self.processes.pop(process_id)
            if block_index in self.available_blocks:
                self.available_blocks[block_index] += size
            else:
                self.available_blocks[block_index] = size
            print(f"Process {process_id} deallocated from Block {block_index}")
        else:
            print(f"Process {process_id} not found")

    def display_memory_status(self):
        print("Current Memory Allocation Status:")
        for index, block_size in self.available_blocks.items():
            print(f"Block {index}: {block_size} KB free")
        for process_id, (block_index, size) in self.processes.items():
            print(f"Process {process_id}: {size} KB in Block {block_index}")

# Driver Code
memory_manager = WorstFitMemoryManager([150, 300, 100, 200, 250, 50, 350, 180, 120, 200])
memory_manager.allocate_memory(1, 180)
memory_manager.allocate_memory(2, 400)
memory_manager.allocate_memory(3, 120)
memory_manager.display_memory_status()
memory_manager.deallocate_memory(2)
print("\nAfter deallocating Process 2:")
memory_manager.display_memory_status()
