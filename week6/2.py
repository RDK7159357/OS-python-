class Page:
    def __init__(self, page_id, process_name=None):
        """Initialize a page with an ID and optional process name."""
        self.page_id = page_id
        self.process_name = process_name

    def allocate(self, process_name):
        """Allocate the page to a specific process."""
        self.process_name = process_name

    def deallocate(self):
        """Deallocate the page, making it available."""
        self.process_name = None

    def __str__(self):
        """String representation of the page status."""
        return f"Page {self.page_id}: {self.process_name or 'Free'}"


class MemoryManager:
    def __init__(self, num_pages, page_size):
        """Initialize the memory manager with pages and page size."""
        self.num_pages = num_pages
        self.page_size = page_size
        self.pages = [Page(page_id) for page_id in range(num_pages)]

    def allocate_memory(self, process_name, num_pages_requested):
        """Allocate pages to a process if enough pages are available."""
        free_pages = [page for page in self.pages if page.process_name is None]

        if len(free_pages) >= num_pages_requested:
            for i in range(num_pages_requested):
                free_pages[i].allocate(process_name)
            return True  # Allocation successful
        else:
            return False  # Not enough free pages

    def print_memory_status(self):
        """Print the status of all pages."""
        print("\nMemory Status:")
        for page in self.pages:
            print(page)

    def print_total_memory_used(self):
        """Print the total memory used in KB."""
        used_pages = sum(1 for page in self.pages if page.process_name is not None)
        total_memory_used = used_pages * self.page_size
        print(f"\nTotal memory used: {total_memory_used} KB\n")


# Driver Code
memory_manager = MemoryManager(num_pages=200, page_size=8)  # Page size = 8 KB

requests = [
    ("Student Records System", 40),
    ("Faculty Management System", 25),
    ("Library Information System", 30),
    ("Online Learning Platform", 35),
    ("Research Database", 50)
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
