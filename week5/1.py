def worst_fit_allocation(memory_blocks, program_requests):
    allocations = {}  # Store allocations for each program

    for program, request in program_requests.items():
        # Find the block with the maximum available memory that can fit the request
        worst_block_index = -1
        max_block_size = -1
        
        for i in range(len(memory_blocks)):
            if memory_blocks[i] >= request and memory_blocks[i] > max_block_size:
                max_block_size = memory_blocks[i]
                worst_block_index = i

        # If a suitable block is found, allocate memory
        if worst_block_index != -1:
            allocations[program] = request
            memory_blocks[worst_block_index] -= request
        else:
            allocations[program] = "Not allocated"  # Couldn't allocate memory

    return allocations, memory_blocks


# Driver Code
memory_blocks = [400, 250, 350, 200, 150]
program_requests = {'Program A': 150, 'Program B': 300, 'Program C': 200}

allocations, remaining_memory = worst_fit_allocation(memory_blocks, program_requests)

# Output the allocations
for program, allocated_memory in allocations.items():
    print(f"{program} allocated {allocated_memory} units of memory.")

print("\nRemaining Memory in Memory Blocks:")
for i in range(len(memory_blocks)):
    print(f"Block {i+1}: {memory_blocks[i]} units")
