class OperatingSystem:
    def __init__(self, total_blocks):
        self.total_blocks = total_blocks
        self.disk_blocks = [False] * total_blocks  # False indicates block is free
        self.index = {}  # Maps file names to allocated blocks

    def calculate_blocks_needed(self, file_size):
        return (file_size + 1023) // 1024  # Assuming each block is 1 MB

    def find_free_blocks(self, required_blocks):
        free_blocks = [i for i, block in enumerate(self.disk_blocks) if not block]
        if len(free_blocks) >= required_blocks:
            return free_blocks[:required_blocks]
        return []

    def allocate_blocks(self, file_name, file_size):
        blocks_needed = self.calculate_blocks_needed(file_size)
        free_blocks = self.find_free_blocks(blocks_needed)

        if not free_blocks:
            print(f"Not enough free blocks to allocate {file_name}")
            return

        for block in free_blocks:
            self.disk_blocks[block] = True

        self.index[file_name] = free_blocks
        print(f"Allocated {blocks_needed} blocks to {file_name}")

    def delete_file(self, file_name):
        if file_name in self.index:
            for block in self.index[file_name]:
                self.disk_blocks[block] = False
            del self.index[file_name]
            print(f"Deleted {file_name}")
        else:
            print(f"{file_name} not found")

    def total_free_blocks(self):
        return sum(1 for block in self.disk_blocks if not block)

    def display_allocation_status(self):
        print("\nAllocation Status:")
        for i, block in enumerate(self.disk_blocks):
            status = "Allocated" if block else "Free"
            print(f"Block {i}: {status}")
        print(f"\nTotal Free Blocks: {self.total_free_blocks()}")

# Driver Code
os = OperatingSystem(1000)

os.allocate_blocks("database.db", 300)
os.allocate_blocks("video.mp4", 600)
os.allocate_blocks("image.jpg", 150)

os.display_allocation_status()

os.delete_file("video.mp4")

print("\nAfter deleting video.mp4:")
os.display_allocation_status()
