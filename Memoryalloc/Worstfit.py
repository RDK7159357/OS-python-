class WorstFit:
    def __init__(self, total_memory):
        self.total_memory = total_memory
        self.free_memory = total_memory
        self.partitions = []
        self.allocated = {}

    def allocate(self, pid, size):
        # Worst Fit: Allocate to the largest partition
        worst_index = -1
        worst_size = 0
        
        for i, free_space in enumerate(self.partitions):
            if free_space >= size and free_space > worst_size:
                worst_index = i
                worst_size = free_space
        
        # If no existing partition fits, create a new one
        if worst_index == -1:
            if self.free_memory >= size:
                self.partitions.append(size)
                worst_index = len(self.partitions) - 1
            else:
                print(f"Not enough memory for Process {pid}")
                return False
        
        # Allocate memory
        self.partitions[worst_index] -= size
        self.allocated[pid] = (worst_index, size)
        self.free_memory -= size
        print(f"Allocated {size} to Process {pid}")
        return True

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
print("\nWorst Fit Allocation:")
worst_fit = WorstFit(100)
worst_fit.allocate("P1", 30)
worst_fit.allocate("P2", 40)
worst_fit.display()
worst_fit.deallocate("P1", 30)
worst_fit.allocate("P3", 20)
worst_fit.display()