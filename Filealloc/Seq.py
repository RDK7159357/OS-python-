class SequentialAllocation:
    def __init__(self, disk_size):
        self.disk = [None] * disk_size  # Represent disk as an array of blocks
    
    def allocate(self, file_name, start, size):
        if any(self.disk[start:start + size]):
            print(f"Error: Not enough contiguous space for file {file_name}")
            return False
        self.disk[start:start + size] = [file_name] * size
        print(f"File {file_name} allocated sequentially from block {start} to {start + size - 1}")
        return True

    def display(self):
        print("Disk Blocks:", self.disk)

# Sequential Allocation example usage
print("Sequential Allocation")
seq_alloc = SequentialAllocation(20)
seq_alloc.allocate("A", 0, 5)
seq_alloc.allocate("B", 6, 4)
seq_alloc.display()
