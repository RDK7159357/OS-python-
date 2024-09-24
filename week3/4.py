class DigitalArchive:
    def __init__(self, total_blocks):
        self.total_blocks = total_blocks
        self.disk_blocks = [None] * total_blocks  # Track file allocations
        self.file_table = {}  # Keep track of file allocations

    def calculate_blocks_needed(self, file_size):
        return (file_size + 1023) // 1024  # Assuming each block is 1 MB

    def allocate_blocks(self, file_name, file_size):
        blocks_needed = self.calculate_blocks_needed(file_size)
        free_blocks = [i for i, block in enumerate(self.disk_blocks) if block is None]

        if len(free_blocks) < blocks_needed:
            print(f"Not enough space to allocate {file_name}")
            return

        allocated_blocks = free_blocks[:blocks_needed]
        for block in allocated_blocks:
            self.disk_blocks[block] = file_name

        self.file_table[file_name] = allocated_blocks
        print(f"Allocated {blocks_needed} blocks to {file_name}")

    def delete_file(self, file_name):
        if file_name in self.file_table:
            for block in self.file_table[file_name]:
                self.disk_blocks[block] = None
            del self.file_table[file_name]
            print(f"Deleted {file_name}")
        else:
            print(f"{file_name} not found")

    def display_allocation_status(self):
        print("\nCurrent Allocation Status:")
        for i, file in enumerate(self.disk_blocks):
            status = file if file else "Free"
            print(f"Block {i}: {status}")

# Driver Code
digital_archive = DigitalArchive(100)

digital_archive.allocate_blocks("Portrait1.jpg", 15 * 1024)  # Size in KB
digital_archive.allocate_blocks("Landscape1.jpg", 10 * 1024)  # Size in KB
digital_archive.allocate_blocks("Architecture1.jpg", 7 * 1024)  # Size in KB

digital_archive.display_allocation_status()

digital_archive.delete_file("Landscape1.jpg")

print("\nAfter deleting Landscape1.jpg:")
digital_archive.display_allocation_status()
