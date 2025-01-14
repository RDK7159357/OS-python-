def worst_fit(memory_blocks, processes):
    allocation = []
    for process in processes:
        # Find the block with the largest size that can accommodate the process
        worst_idx = next(
            (i for i, block in sorted(enumerate(memory_blocks), key=lambda x: -x[1]) if block >= process), 
            -1
        )
        if worst_idx != -1:
            memory_blocks[worst_idx] -= process
        allocation.append(worst_idx)

    for i, alloc in enumerate(allocation):
        print(f"Process {i} -> Block {alloc if alloc != -1 else 'Not Allocated'}")

# Example usage
memory = [100, 500, 200, 300, 600]
processes = [212, 417, 112, 426]
worst_fit(memory, processes)


def first_fit(memory_blocks, processes):
    allocation = []
    for process in processes:
        # Find the first block that can accommodate the process
        first_idx = next((i for i, block in enumerate(memory_blocks) if block >= process), -1)
        if first_idx != -1:
            memory_blocks[first_idx] -= process
        allocation.append(first_idx)

    for i, alloc in enumerate(allocation):
        print(f"Process {i} -> Block {alloc if alloc != -1 else 'Not Allocated'}")

# Example usage
memory_blocks = [100, 500, 200, 300, 600]
process_list = [212, 417, 112, 426]
first_fit(memory_blocks, process_list)
