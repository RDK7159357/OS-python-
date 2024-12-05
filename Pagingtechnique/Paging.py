class Paging:
    def __init__(self, memory_size, page_size):
        self.memory_size = memory_size
        self.page_size = page_size
        self.num_pages = memory_size // page_size
        self.page_table = [None] * self.num_pages

    def allocate(self, pid, num_pages_needed):
        free_pages = [i for i, page in enumerate(self.page_table) if page is None]
        if len(free_pages) >= num_pages_needed:
            allocated_pages = free_pages[:num_pages_needed]
            for page in allocated_pages:
                self.page_table[page] = pid
            print(f"Process {pid} allocated pages: {allocated_pages}")
        else:
            print(f"Error: Not enough pages for Process {pid}.")

    def deallocate(self, pid):
        deallocated_pages = [i for i, page in enumerate(self.page_table) if page == pid]
        for page in deallocated_pages:
            self.page_table[page] = None
        print(f"Process {pid} deallocated pages: {deallocated_pages}")

    def display(self):
        print("Page Table:", self.page_table)

# Example usage
if __name__ == "__main__":
    paging = Paging(memory_size=100, page_size=10)
    paging.allocate("P1", 3)
    paging.allocate("P2", 5)
    paging.display()
    paging.deallocate("P1")
    paging.display()
