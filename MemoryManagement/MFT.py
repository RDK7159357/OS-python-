class MFT:
    def __init__(self, total_memory, partition_size):
        self.total_memory = total_memory
        self.partition_size = partition_size
        self.partitions = [None] * (total_memory // partition_size)  # Fixed number of partitions

    def allocate(self, pid):
        for i in range(len(self.partitions)):
            if self.partitions[i] is None:  # Find empty partition
                self.partitions[i] = pid
                print(f"Process {pid} allocated to partition {i}.")
                return
        print(f"Error: No space for Process {pid}.")

    def deallocate(self, pid):
        for i in range(len(self.partitions)):
            if self.partitions[i] == pid:
                self.partitions[i] = None  # Deallocate process
                print(f"Process {pid} deallocated from partition {i}.")
                return
        print(f"Error: Process {pid} not found.")

    def display(self):
        print(f"Partitions: {self.partitions}")
# Example usage
mft = MFT(100, 20)
mft.allocate("P1")
mft.allocate("P2")
mft.display()
mft.deallocate("P1")
mft.display()
