class PagingMemoryManager:
    def __init__(self, num_pages, page_size):
        self.num_pages = num_pages
        self.page_size = page_size
        self.available_pages = [True] * num_pages
        self.processes = {}

    def allocate_memory(self, process_id, size):
        num_required_pages = (size + self.page_size - 1) // self.page_size  # Calculate the number of pages needed
        allocated_pages = []

        for i in range(self.num_pages):
            if len(allocated_pages) == num_required_pages:
                break
            if self.available_pages[i]:
                self.available_pages[i] = False
                allocated_pages.append(i)

        if len(allocated_pages) == num_required_pages:
            self.processes[process_id] = allocated_pages
            print(f"Allocated pages {allocated_pages} to process {process_id}.")
            return True
        else:
            # Rollback allocation if not enough pages are available
            for page in allocated_pages:
                self.available_pages[page] = True
            print(f"Not enough pages available for process {process_id}.")
            return False

    def deallocate_memory(self, process_id):
        if process_id in self.processes:
            allocated_pages = self.processes.pop(process_id)
            for page in allocated_pages:
                self.available_pages[page] = True
            print(f"Deallocated pages {allocated_pages} from process {process_id}.")
        else:
            print(f"Process {process_id} not found.")

    def display_memory_status(self):
        print("Memory Status:")
        for i in range(self.num_pages):
            status = "Free" if self.available_pages[i] else "Occupied"
            print(f"Page {i}: {status}")

# Driver Code
memory_manager = PagingMemoryManager(num_pages=20, page_size=200)
memory_manager.allocate_memory(1, 400)
memory_manager.allocate_memory(2, 600)
memory_manager.allocate_memory(3, 300)
memory_manager.display_memory_status()
memory_manager.deallocate_memory(2)
print("\nAfter deallocating Process 2:")
memory_manager.display_memory_status()
