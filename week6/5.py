class Page:
    def __init__(self, page_id, process_name=None):
        """Initialize a page with an ID and optional process_name."""
        self.page_id = page_id
        self.process_name = process_name

    def allocate(self, process_name):
        """Allocate the page to a given process."""
        self.process_name = process_name

    def deallocate(self):
        """Deallocate the page, making it available."""
        self.process_name = None

    def __str__(self):
        """Return a string representation of the page."""
        status = f"Page {self.page_id}: "
        if self.process_name:
            status += f"Allocated to {self.process_name}"
        else:
            status += "Free"
        return status


class MemoryManager:
    def __init__(self, num_pages, page_size):
        """Initialize memory with a given number of pages and page size."""
        self.pages = [Page(page_id) for page_id in range(num_pages)]
        self.page_size = page_size  # Page size isn't actively used but could be useful for extensions

    def allocate_memory(self, process_name, num_pages_requested):
        """Allocate memory to a process if enough free pages are available."""
        free_pages = [page for page in self.pages if page.process_name is None]

        if len(free_pages) >= num_pages_requested:
            # Allocate requested number of pages to the process
            for i in range(num_pages_requested):
                free_pages[i].allocate(process_name)
            return True
        else:
            return False

    def print_memory_status(self):
        """Print the status of all pages."""
        print("Memory Status:")
        for page in self.pages:
            print(page)

    def print_total_memory_used(self):
        """Print the total memory used by all processes."""
        used_pages = sum(1 for page in self.pages if page.process_name)
        print(f"Total Memory Used: {used_pages} pages")


# Driver Code
memory_manager = MemoryManager(num_pages=512, page_size=1)

requests = [
    ("Product Catalog Management", 80),
    ("Order Processing System", 120),
    ("Customer Database", 150),
    ("Payment Processing Gateway", 100),
    ("Inventory Tracking System", 60)
]

for process_name, num_pages_requested in requests:
    allocated = memory_manager.allocate_memory(process_name, num_pages_requested)
    if allocated:
        print(f"Allocated {num_pages_requested} pages for {process_name}")
        memory_manager.print_memory_status()
    else:
        print(f"Not enough memory available for {process_name} (requested {num_pages_requested} pages)")

memory_manager.print_total_memory_used()
