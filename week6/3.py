class Page:
    def __init__(self, page_id, process_name=None):
        """Initialize a page with its ID and an optional process name."""
        self.page_id = page_id
        self.process_name = process_name

    def allocate(self, process_name):
        """Allocate the page to the specified process."""
        self.process_name = process_name

    def deallocate(self):
        """Deallocate the page, making it available for future use."""
        self.process_name = None

    def __str__(self):
        """Return a string representation of the page's status."""
        return f"Page {self.page_id}: {self.process_name or 'Free'}"


class MemoryManager:
    def __init__(self, num_pages, page_size):
        """Initialize the memory manager with the given pages and page size."""
        self.num_pages = num_pages
        self.page_size = page_size  # in KB
        self.pages = [Page(page_id) for page_id in range(num_pages)]

    def allocate_memory(self, process_name, num_pages_requested):
        """Allocate the requested number of pages to a process."""
        free_pages = [page for page in self.pages if page.process_name is None]

        if len(free_pages) >= num_pages_requested:
            # Allocate the requested pages to the process
            for i in range(num_pages_requested):
                free_pages[i].allocate(process_name)
            return True  # Allocation successful
        else:
            return False  # Not enough free pages

    def print_memory_status(self):
        """Print the status of each page in memory."""
        print("\nMemory Status:")
        for page in self.pages:
            print(page)

    def print_total_memory_used(self):
        """Print the total memory used in KB."""
        used_pages = sum(1 for page in self.pages if page.process_name is not None)
        total_memory_used = used_pages * self.page_size
        print(f"\nTotal Memory Used: {total_memory_used} KB\n")


# Driver Code
memory_manager = MemoryManager(num_pages=256, page_size=16)  # 256 pages, each 16 KB

requests = [
    ("Game Session 1", 32),
    ("Game Session 2", 20),
    ("Game Session 3", 40),
    ("Game Session 4", 18),
    ("Game Session 5", 25)
]

for request in requests:
    process_name, num_pages_requested = request
    allocated = memory_manager.allocate_memory(process_name, num_pages_requested)

    if allocated:
        print(f"Allocated {num_pages_requested} pages for {process_name}")
    else:
        print(f"Not enough memory available for {process_name} (requested {num_pages_requested} pages)")

    memory_manager.print_memory_status()

memory_manager.print_total_memory_used()
