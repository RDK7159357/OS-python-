def lru_replacement(pages, capacity):
    # Initialize an empty list to store pages in order of usage
    memory, faults = [], 0

    for pg in pages:  # Iterate through each page request
        if pg in memory:  # If the page is already in memory
            memory.remove(pg)  # Remove it to update its position
        else:  # If the page is not in memory (page fault)
            faults += 1  # Increment page fault counter
            if len(memory) == capacity:  # If memory is full
                memory.pop(0)  # Remove the least recently used page
        memory.append(pg)  # Add the current page to memory (most recently used)

    return faults  # Return total page faults

# Example usage
pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
capacity = 3
print("LRU Faults:", lru_replacement(pages, capacity))
