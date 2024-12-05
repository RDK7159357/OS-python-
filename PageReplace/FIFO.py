from collections import deque

def fifo_replacement(pages, capacity):
    # Initialize an empty queue (memory) to store pages in FIFO order
    memory, faults = deque(), 0

    for pg in pages:  # Iterate through each page request
        if pg not in memory:  # If the page is not in memory (page fault)
            faults += 1  # Increment page fault counter
            if len(memory) == capacity:  # If memory is full
                memory.popleft()  # Remove the oldest page (FIFO policy)
            memory.append(pg)  # Add the new page to memory

    return faults  # Return total page faults

# Example usage
pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
capacity = 3
print("FIFO Faults:", fifo_replacement(pages, capacity))
