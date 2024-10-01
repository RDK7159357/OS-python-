class MemoryBlock:
    def __init__(self, start, size):
        self.start = start
        self.size = size
        self.allocated = False
        self.process_name = None

    def is_free(self):
        return not self.allocated

    def allocate(self, process_name):
        if self.is_free():
            self.allocated = True
            self.process_name = process_name
            return True
        return False

    def deallocate(self):
        self.allocated = False
        self.process_name = None

    def __str__(self):
        status = "Free" if not self.allocated else f"Allocated to {self.process_name}"
        return f"[Start: {self.start}, Size: {self.size}, Status: {status}]"


class MemoryManager:
    def __init__(self, total_memory):
        self.total_memory = total_memory
        self.memory_blocks = [MemoryBlock(0, total_memory)]

    def allocate_memory(self, process_name, size):
        for block in self.memory_blocks:
            if block.is_free() and block.size >= size:
                if block.size > size:
                    # Split the block
                    new_block = MemoryBlock(block.start + size, block.size - size)
                    self.memory_blocks.insert(self.memory_blocks.index(block) + 1, new_block)
                block.size = size
                block.allocate(process_name)
                print(f"Allocated {size} units to {process_name}.")
                return True
        print(f"Failed to allocate {size} units to {process_name}.")
        return False

    def deallocate_memory(self, process_name):
        for block in self.memory_blocks:
            if block.allocated and block.process_name == process_name:
                block.deallocate()
                print(f"Deallocated memory for {process_name}.")
                self.merge_free_blocks()  # Merge free blocks if possible
                return True
        print(f"Process {process_name} not found.")
        return False

    def merge_free_blocks(self):
        i = 0
        while i < len(self.memory_blocks) - 1:
            current_block = self.memory_blocks[i]
            next_block = self.memory_blocks[i + 1]
            if current_block.is_free() and next_block.is_free():
                # Merge adjacent free blocks
                current_block.size += next_block.size
                del self.memory_blocks[i + 1]  # Remove the next block after merging
            else:
                i += 1

    def print_memory_status(self):
        print("\nMemory Status:")
        for block in self.memory_blocks:
            print(block)

    def print_total_memory_used(self):
        used_memory = sum(block.size for block in self.memory_blocks if not block.is_free())
        print(f"\nTotal Memory Used: {used_memory}/{self.total_memory} units\n")


# Driver Code
memory_manager = MemoryManager(8000)
requests = [("SubsysA", 1500), ("SubsysB", 1000), ("SubsysC", 700), 
            ("SubsysD", 2200), ("SubsysE", 500), ("SubsysF", 1200)]

for request in requests:
    process_name, size = request
    allocated = memory_manager.allocate_memory(process_name, size)
    if allocated:
        memory_manager.print_memory_status()
        memory_manager.print_total_memory_used()
