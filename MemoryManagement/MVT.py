# MVT - Multiple Variable Partition
class MVT:
    def __init__(self, total_memory):
        self.total_memory = total_memory
        self.free_memory = total_memory
        self.partitions = []

    def allocate(self, pid, size):
        if size <= self.free_memory:
            self.partitions.append((pid, size))
            self.free_memory -= size
            print(f"Process {pid} allocated {size} units.")
        else:
            print(f"Error: Not enough memory for Process {pid}.")

    def deallocate(self, pid):
        for i, (p, size) in enumerate(self.partitions):
            if p == pid:
                self.free_memory += size
                self.partitions.pop(i)
                print(f"Process {pid} deallocated.")
                return
        print(f"Error: Process {pid} not found.")

    def display(self):
        print(f"Free: {self.free_memory}, Allocated: {self.partitions}")

print("MVT - Multiple Variable Partition:")
mvt = MVT(100)
mvt.allocate("P1", 30)
mvt.allocate("P2", 40)
mvt.display()
mvt.deallocate("P1")
mvt.allocate("P3", 50)
mvt.display()