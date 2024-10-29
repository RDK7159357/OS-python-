class Page:
    def __init__(self, page_id, process_name=None):
        """Initialize a page with a unique ID and an optional process name."""
        self.page_id = page_id
        self.process_name = process_name

    def allocate(self, process_name):
        """Allocate the page to the given process."""
        self.process_name = process_name

    def deallocate(self):
        """Deallocate the page, making it free."""
        self.process_name = None

    def __str__(self):
        """Return a string representation of the page."""
        return f"Page {self.page_id}: {self.process_name or 'Free'}"

class MemoryManager:
    def __init__(self, num_pages, page_size):
        """Initialize the memory manager with given number of pages and page size."""
        self.num_pages = num_pages
        self.page_size = page_size
        self.pages = [Page(page_id) for page_id in range(num_pages)]

    def allocate_memory(self, process_name, num_pages_requested):
        """Allocate the requested number of pages to a process."""
        free_pages = [page for page in self.pages if page.process_name is None]

        if len(free_pages) >= num_pages_requested:
            for i in range(num_pages_requested):
                free_pages[i].allocate(process_name)
            return True  # Allocation successful
        else:
            return False  # Not enough free pages

    def print_memory_status(self):
        """Print the status of each page."""
        for page in self.pages:
            print(page)

    def print_total_memory_used(self):
        """Print the total memory used by all allocated pages."""
        used_pages = sum(1 for page in self.pages if page.process_name is not None)
        total_memory_used = used_pages * self.page_size
        print(f"Total memory used: {total_memory_used} KB")

# Driver Code
memory_manager = MemoryManager(num_pages=100, page_size=4)  # 4 KB page size
requests = [
    ("Process A", 25),
    ("Process B", 15),
    ("Process C", 30),
    ("Process D", 12),
    ("Process E", 20)
]

for request in requests:
    process_name, num_pages_requested = request
    allocated = memory_manager.allocate_memory(process_name, num_pages_requested)
    
    if allocated:
        print(f"Allocated {num_pages_requested} pages for {process_name}")
    else:
        print(f"Not enough memory available for {process_name} (requested {num_pages_requested} pages)")

    memory_manager.print_memory_status()
    print()

memory_manager.print_total_memory_used()
