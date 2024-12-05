def optimal_replacement(pages, capacity):
    memory, faults = [], 0

    for i, pg in enumerate(pages):  # Iterate through page requests
        if pg not in memory:  # Page fault occurs
            faults += 1
            if len(memory) == capacity:  # Memory is full
                # Find the page to replace
                future_use = [pages[i + 1:].index(x) if x in pages[i + 1:] else float('inf') for x in memory]
                memory.pop(future_use.index(max(future_use)))  # Remove page used farthest in the future
            memory.append(pg)  # Add the new page to memory
    return faults

# Example usage
pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
capacity = 3
print("Optimal Faults:", optimal_replacement(pages, capacity))
