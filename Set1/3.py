# 3. Memory Allocation using Best-Fit Algorithm
def best_fit(memory_blocks, processes):
    allocation = []
    for process in processes:
        best_idx = next((i for i, block in sorted(enumerate(memory_blocks), key=lambda x: x[1]) if block >= process), -1)
        if best_idx != -1:
            memory_blocks[best_idx] -= process
        allocation.append(best_idx)

    for i, alloc in enumerate(allocation):
        print(f"Process {i} -> Block {alloc if alloc != -1 else 'Not Allocated'}")

memory = [100, 500, 200, 300, 600]
processes = [212, 417, 112, 426]
best_fit(memory, processes)