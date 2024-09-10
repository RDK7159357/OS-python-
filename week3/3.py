from threading import Semaphore

class DiskBlock:
    def __init__(self, block_id):
        self.block_id = block_id
        self.next_block = None
        self.semaphore = Semaphore(1)

class MediaFile:
    def __init__(self, file_name, size):
        self.file_name = file_name
        self.size = size
        self.start_block = None

class FileAllocationTable:
    def __init__(self):
        self.fat = {}

    def allocate_blocks(self, media_file, disk_blocks):
        num_blocks_required = (media_file.size + 1023) // 1024

        if len(disk_blocks) < num_blocks_required:
            print("Not enough free blocks to allocate")
            return False

        # Allocate blocks and create linked list
        current_block = None
        for _ in range(num_blocks_required):
            block = disk_blocks.pop(0)
            if not current_block:
                media_file.start_block = block
            else:
                current_block.next_block = block
            current_block = block

        self.fat[media_file.file_name] = media_file.start_block.block_id
        return True

    def delete_file(self, media_file, disk_blocks):
        current_block = media_file.start_block
        while current_block:
            disk_blocks.append(current_block)
            current_block = current_block.next_block

        del self.fat[media_file.file_name]

def simulate_file_allocation():
    disk_blocks = [DiskBlock(i) for i in range(10)]
    fat = FileAllocationTable()

    media_file1 = MediaFile("file1.txt", 5)
    media_file2 = MediaFile("file2.mp3", 10)

    fat.allocate_blocks(media_file1, disk_blocks)
    fat.allocate_blocks(media_file2, disk_blocks)

    print("FAT:", fat.fat)

    fat.delete_file(media_file1, disk_blocks)
    print("FAT after deletion:", fat.fat)

simulate_file_allocation()
