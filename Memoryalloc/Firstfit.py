class FirstFit:
    def __init__(self, total_memory):
        self.total_memory = total_memory
        self.free_memory = total_memory
        self.partitions = []
        self.allocated = {}

    def allocate(self, pid, size):
        # First Fit: Allocate to the first partition large enough
        for i, free_space in enumerate(self.partitions):
            if free_space >= size:
                self.partitions[i] -= size
                self.allocated[pid] = (i, size)
                self.free_memory -= size
                print(f"Allocated {size} to Process {pid}")
                return True
        
        # If no existing partition fits, create a new one
        if self.free_memory >= size:
            self.partitions.append(size)
            index = len(self.partitions) - 1
            self.partitions[index] -= size
            self.allocated[pid] = (index, size)
            self.free_memory -= size
            print(f"Allocated {size} to Process {pid}")
            return True
        
        print(f"Not enough memory for Process {pid}")
        return False

    def deallocate(self, pid, size):
        if pid not in self.allocated:
            print(f"Process {pid} not found")
            return False
        
        partition_index, allocated_size = self.allocated[pid]
        self.partitions[partition_index] += size
        self.free_memory += size
        del self.allocated[pid]
        print(f"Deallocated {size} from Process {pid}")
        return True

    def display(self):
        print(f"Free memory: {self.free_memory}")
        print(f"Partitions: {self.partitions}")
        print(f"Allocated: {self.allocated}")
print("First Fit Allocation:")
first_fit = FirstFit(100)
first_fit.allocate("P1", 30)
first_fit.allocate("P2", 40)
first_fit.display()
first_fit.deallocate("P1", 30)
first_fit.allocate("P3", 20)
first_fit.display()