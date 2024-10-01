class OperatingSystem: 
    def __init__(self, total_blocks):
        self.total_blocks = total_blocks 
        self.disk_blocks = [False] * total_blocks    # False indicates block is free 
        self.index = {}    # Index to map file names to their allocated disk blocks

    def allocate_blocks(self, file_name, file_size):
        # Calculate the number of blocks needed
        blocks_needed = self.calculate_blocks_needed(file_size)
        
        # Find available blocks
        free_blocks = self.find_free_blocks(blocks_needed)
        
        if len(free_blocks) < blocks_needed:
            print(f"Not enough blocks available to allocate {file_name}. Needed: {blocks_needed}, Available: {len(free_blocks)}")
            return
        
        # Allocate blocks
        for block in free_blocks[:blocks_needed]:
            self.disk_blocks[block] = True
        
        # Map the file to its allocated blocks
        self.index[file_name] = free_blocks[:blocks_needed]
        print(f"Allocated {blocks_needed} blocks for {file_name}")

    def delete_file(self, file_name):
        if file_name in self.index:
            # Get the blocks allocated to the file
            allocated_blocks = self.index[file_name]
            
            # Free the blocks
            for block in allocated_blocks:
                self.disk_blocks[block] = False
            
            # Remove the file from the index
            del self.index[file_name]
            print(f"Deleted {file_name} and freed its blocks.")
        else:
            print(f"File {file_name} not found.")

    def find_free_blocks(self, required_blocks):
        # Find and return the indices of the free blocks
        free_blocks = [i for i, block in enumerate(self.disk_blocks) if not block]
        return free_blocks

    def calculate_blocks_needed(self, file_size):
        # Assuming each block can hold 1MB, so the number of blocks needed equals the file size in MB
        return file_size

    def total_free_blocks(self):
        # Return the total number of free blocks available
        return self.disk_blocks.count(False)

    def display_allocation_status(self):
        print("\nDisk Allocation Status:")
        free_blocks = self.total_free_blocks()
        occupied_blocks = self.total_blocks - free_blocks
        print(f"Total Blocks: {self.total_blocks}, Occupied Blocks: {occupied_blocks}, Free Blocks: {free_blocks}")

        print("\nFile Allocation Table:")
        if not self.index:
            print("No files are currently allocated.")
        else:
            for file_name, blocks in self.index.items():
                block_range = f"{blocks[0]} - {blocks[-1]}" if len(blocks) > 1 else f"{blocks[0]}"
                print(f"{file_name}: {len(blocks)} blocks, Block Range: {block_range}")

# Driver Code 
os = OperatingSystem(1000)
os.allocate_blocks("database.db", 300)
os.allocate_blocks("video.mp4", 600)
os.allocate_blocks("image.jpg", 150)
os.display_allocation_status()