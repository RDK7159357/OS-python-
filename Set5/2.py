# 14. Paging Memory Management
def paging(memory_size, page_size):
    num_pages = memory_size // page_size
    print(f"Total Pages: {num_pages}")
    for i in range(num_pages):
        print(f"Page {i}: Address {i * page_size}")

paging(1024, 128)