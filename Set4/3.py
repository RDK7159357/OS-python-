# 12. Busy Cafe using LRU Page Replacement Algorithm
def lru_page_replacement(pages, capacity):
    memory = []
    page_faults = 0

    for page in pages:
        if page not in memory:
            page_faults += 1
            if len(memory) >= capacity:
                memory.pop(0)  # Remove least recently used page
            memory.append(page)
        else:
            memory.remove(page)
            memory.append(page)  # Move accessed page to the end

        print(f"Memory: {memory}")

    print(f"Total Page Faults: {page_faults}")

page_requests = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1]
capacity = 3
lru_page_replacement(page_requests, capacity)