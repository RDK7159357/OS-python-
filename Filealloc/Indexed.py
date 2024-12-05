class IndexedAllocation:
    def __init__(self, disk_size):
        self.disk = [None] * disk_size  # Represent disk as an array of blocks
        self.index_blocks = {}  # Store the index blocks for files
    
    def allocate(self, file_name, block_indices):
        if any(self.disk[i] for i in block_indices):
            print(f"Error: Some blocks are already occupied for file {file_name}")
            return False
        self.index_blocks[file_name] = block_indices
        for i in block_indices:
            self.disk[i] = file_name
        print(f"File {file_name} allocated with blocks: {block_indices}")
        return True

    def display(self):
        print("Disk Blocks:", self.disk)
        print("Index Blocks:", self.index_blocks)

# Indexed Allocation example usage
print("\nIndexed Allocation")
indx_alloc = IndexedAllocation(20)
indx_alloc.allocate("C", [2, 5, 8])
indx_alloc.allocate("D", [10, 12, 14])
indx_alloc.display()
