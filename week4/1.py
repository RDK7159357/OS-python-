class MemoryVariableTechnique:
    def __init__(self, partitions):
        self.partitions = partitions
        self.memory_map = {pid: [False] * size for pid, size in partitions.items()}
        self.processes = {}

    def allocate_memory(self, process_id, size):
        for partition_id, partition_size in self.partitions.items():
            if partition_size >= size and not any(self.memory_map[partition_id]):
                self.memory_map[partition_id] = [True] * size + [False] * (partition_size - size)
                self.processes[process_id] = (partition_id, size)
                print(f"Process {process_id} allocated {size} KB in Partition {partition_id}")
                return True
        print(f"Process {process_id} allocation of {size} KB failed")
        return False

    def deallocate_memory(self, process_id):
        if process_id in self.processes:
            partition_id, size = self.processes.pop(process_id)
            self.memory_map[partition_id] = [False] * self.partitions[partition_id]
            print(f"Process {process_id} deallocated from Partition {partition_id}")
        else:
            print(f"Process {process_id} not found")

    def display_memory_status(self):
        print("Current Memory Allocation Status:")
        for partition_id, partition in self.memory_map.items():
            used_space = sum(partition)
            free_space = len(partition) - used_space
            print(f"Partition {partition_id}: {used_space} KB used, {free_space} KB free")

# Driver Code
mvt = MemoryVariableTechnique({1: 300, 2: 500, 3: 200})
mvt.allocate_memory(1, 150)
mvt.allocate_memory(2, 400)
mvt.allocate_memory(3, 100)
mvt.display_memory_status()
mvt.deallocate_memory(2)
print("\nAfter deallocating Process 2:")
mvt.display_memory_status()
