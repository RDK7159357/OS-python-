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
        self.memory_blocks = [MemoryBlock(0, total_memory)]  # Start with one large free block

    def allocate_memory(self, process_name, size):
        for block in self.memory_blocks:
            if block.is_free() and block.size >= size:
                if block.size > size:
                    # Split the block if it's larger than the requested size
                    new_block = MemoryBlock(block.start + size, block.size - size)
                    self.memory_blocks.insert(self.memory_blocks.index(block) + 1, new_block)
                block.size = size
                block.allocate(process_name)
                print(f"Allocated {size} units to {process_name}.")
                return True
        print(f"Failed to allocate {size} units to {process_name}.")
        return False

    def print_memory_status(self):
        print("\nMemory Status:")
        for block in self.memory_blocks:
            print(block)

    def print_total_memory_used(self):
        used_memory = sum(block.size for block in self.memory_blocks if not block.is_free())
        print(f"\nTotal Memory Used: {used_memory}/{self.total_memory} units\n")


# Driver Code
memory_manager = MemoryManager(8000)
requests = [
    ("Emergency Department", 2000),
    ("Cardiology Department", 1500),
    ("Laboratory Information System", 1200),
    ("Radiology Department", 1800),
    ("Patient Management System", 1000),
    ("Pharmacy System", 600),
    ("Surgical Services", 2200)
]

for request in requests:
    process_name, size = request
    allocated = memory_manager.allocate_memory(process_name, size)
    if allocated:
        memory_manager.print_memory_status()
        memory_manager.print_total_memory_used()
