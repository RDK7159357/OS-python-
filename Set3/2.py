# 8. Memory Allocation using Worst-Fit Algorithm
def worst_fit(memory_blocks, processes):
    allocation = []
    for process in processes:
        worst_idx = -1
        for i, block in enumerate(memory_blocks):
            if block >= process and (worst_idx == -1 or memory_blocks[worst_idx] < block):
                worst_idx = i
        if worst_idx != -1:
            memory_blocks[worst_idx] -= process
        allocation.append(worst_idx)

    for i, alloc in enumerate(allocation):
        print(f"Process {i} -> Block {alloc if alloc != -1 else 'Not Allocated'}")

memory = [100, 500, 200, 300, 600]
processes = [212, 417, 112, 426]
worst_fit(memory, processes)