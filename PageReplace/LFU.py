from collections import Counter

def lfu_replacement(pages, capacity):
    # Initialize a set for memory and a Counter to track page frequencies
    memory, freq, faults = set(), Counter(), 0

    for pg in pages:  # Iterate through each page request
        if pg not in memory:  # If the page is not in memory (page fault)
            faults += 1  # Increment page fault counter
            if len(memory) == capacity:  # If memory is full
                # Find the least frequently used page (breaking ties by order)
                lfu_page = min(memory, key=lambda x: (freq[x], pages.index(x)))
                memory.remove(lfu_page)  # Remove the least frequently used page
            memory.add(pg)  # Add the new page to memory
        freq[pg] += 1  # Increment the frequency of the current page

    return faults  # Return total page faults

# Example usage
pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
capacity = 3
print("LFU Faults:", lfu_replacement(pages, capacity))
