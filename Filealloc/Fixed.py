class FixedAllocation:
    def __init__(self, num_partitions):
        self.partitions = [None] * num_partitions  # Represent partitions as an array
    
    def allocate(self, file_name, partition):
        if partition >= len(self.partitions) or self.partitions[partition] is not None:
            print(f"Error: Partition {partition} is already occupied or invalid for file {file_name}")
            return False
        self.partitions[partition] = file_name
        print(f"File {file_name} allocated to partition {partition}")
        return True

    def display(self):
        print("Partitions:", self.partitions)

# Fixed Allocation example usage
print("\nFixed Allocation")
fixed_alloc = FixedAllocation(10)
fixed_alloc.allocate("E", 2)
fixed_alloc.allocate("F", 4)
fixed_alloc.display()
