class BestFit:
    def __init__(self, total_memory):
        self.total_memory = total_memory
        self.free_memory = total_memory
        self.partitions = []
        self.allocated = {}

    def allocate(self, pid, size):
        # Find best fit partition
        best_index = -1
        best_size = float('inf')
        
        for i, free_space in enumerate(self.partitions):
            if free_space >= size and free_space < best_size:
                best_index = i
                best_size = free_space
        
        # No suitable partition found
        if best_index == -1:
            if self.free_memory >= size:
                self.partitions.append(size)
                best_index = len(self.partitions) - 1
            else:
                print(f"Not enough memory for Process {pid}")
                return False
        
        # Allocate memory
        self.partitions[best_index] -= size
        self.allocated[pid] = (best_index, size)
        self.free_memory -= size
        
        print(f"Allocated {size} to Process {pid}")
        return True

    def deallocate(self, pid, size):
        if pid not in self.allocated:
            print(f"Process {pid} not found")
            return False
        
        partition_index, allocated_size = self.allocated[pid]
        
        # Return memory to partition
        self.partitions[partition_index] += size
        self.free_memory += size
        del self.allocated[pid]
        
        print(f"Deallocated {size} from Process {pid}")
        return True

    def display(self):
        print(f"Free memory: {self.free_memory}")
        print(f"Partitions: {self.partitions}")
        print(f"Allocated: {self.allocated}")

# Example usage
memory = BestFit(100)
memory.allocate("P1", 30)
memory.allocate("P2", 40)
memory.display()
memory.deallocate("P1", 30)
memory.allocate("P3", 20)
memory.display()