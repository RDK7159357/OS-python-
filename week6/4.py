class Page:
    def __init__(self, page_id, process_name=None):
        """Initialize a page with its ID and an optional process name."""
        self.page_id = page_id
        self.process_name = process_name

    def allocate(self, process_name):
        """Allocate the page to a process."""
        self.process_name = process_name

    def deallocate(self):
        """Deallocate the page, marking it as free."""
        self.process_name = None

    def __str__(self):
        """Return a string representation of the page's status."""
        return f"Page {self.page_id}: {self.process_name or 'Free'}"


class MemoryManager:
    def __init__(self, num_pages, page_size):
        """Initialize memory manager with given number of pages and page size."""
        self.num_pages = num_pages
        self.page_size = page_size  # in KB
        self.pages = [Page(page_id) for page_id in range(num_pages)]

    def allocate_memory(self, process_name, num_pages_requested):
        """Allocate memory pages to a process if enough pages are available."""
        free_pages = [page for page in self.pages if page.process_name is None]

        if len(free_pages) >= num_pages_requested:
            # Allocate the requested number of pages to the process
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
        print(f"\nTotal Memory Used: {total_memory_used} KB\n")


# Driver Code
memory_manager = MemoryManager(num_pages=300, page_size=1)  # 300 pages, each 1 KB

requests = [
    ("Emergency Department", 50),
    ("Radiology Department", 35),
    ("Laboratory Department", 45),
    ("Patient Records System", 60),
    ("Surgery Department", 40)
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
