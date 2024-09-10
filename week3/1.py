# class StudentRecord:
#     def __init__(self, name, student_id, grade, address):
#         self.name = name
#         self.student_id = student_id
#         self.grade = grade
#         self.address = address

#     def __str__(self):
#         return f"Name: {self.name}, ID: {self.student_id}, Grade: {self.grade}, Address: {self.address}"

# class SequentialFileAllocation:
#     def __init__(self, block_size):
#         self.disk_blocks = []
#         self.fat = {}
#         self.block_size = block_size
#         self.next_free_block = 0

#     def calculate_record_size(self, student_record):
#         # Calculate the size of the record in blocks
#         record_size = len(str(student_record)) // self.block_size + 1
#         return record_size

#     def add_record(self, student_record):
#         record_size = self.calculate_record_size(student_record)
#         if self.next_free_block + record_size > len(self.disk_blocks):
#             # Not enough free blocks, return False
#             return False
#         start_block = self.next_free_block
#         self.next_free_block += record_size
#         self.fat[student_record.student_id] = (start_block, record_size)
#         self.disk_blocks.extend([''] * record_size)
#         for i, block in enumerate(str(student_record)):
#             self.disk_blocks[start_block + i % self.block_size] += block
#         return True

#     def get_record(self, student_id):
#         if student_id not in self.fat:
#             return None
#         start_block, record_size = self.fat[student_id]
#         record = ''.join(self.disk_blocks[start_block:start_block + record_size])
#         return StudentRecord(*record.split(', '))

#     def print_disk_status(self):
#         print("Disk Status:")
#         for i, block in enumerate(self.disk_blocks):
#             print(f"Block {i}: {block}")

# # Driver Code
# block_size = 1
# file_system = SequentialFileAllocation(block_size)
# student_records = [
#     StudentRecord("John Doe", 101, 10, "123 Main Street"),
#     StudentRecord("Jane Smith", 102, 11, "456 Elm Street"),
#     StudentRecord("Michael Brown", 103, 9, "789 Oak Avenue")
# ]
# for record in student_records:
#     file_system.add_record(record)
# file_system.print_disk_status()
# student_id = 102
# retrieved_record = file_system.get_record(student_id)
# if retrieved_record:
#     print(f"\nRetrieved Record for ID {student_id}:")
#     print(retrieved_record)
# else:
#     print(f"\nRecord with ID {student_id} not found.")

###########################################################

class StudentRecord:
    def __init__(self, name, student_id, grade,address):
        self.name=name
        self.student_id=student_id
        self.grade=grade
        self.address=address
    def __str__(self):
        return f"Name: {self.name}, ID: {self.student_id}, Grade: {self.grade}, Address: {self.address}"
class SequentialFileAllocation:
    def __init__(self,block_size):
        self.block_size=block_size
        self.fat={}
        self.next_free_block=0
    def add_record(self,student_record):
        self.fat[self.next_free_block]=None
        block_number=self.next_free_block
        self.next_free_block+=1
        with open(f"student_record_{block_number}.txt","w") as file:
            file.write(str(student_record))
        return True
    def get_record(self,student_id):
        for i in range(len(self.fat)):
            with open(f"student_record_{i}.txt","r") as file:
                record=file.read()
                fields=record.split(", ")
                student_id_field=fields[1].split(": ")[1]
                if student_id_field==str(student_id):
                    return record
        return None
    def calculate_record_size(self,student_record):
        record_size=len(str(student_record))
        return (record_size//self.block_size)+1
    def print_disk_status(self):
        print(f"Next free block: {self.next_free_block}")
block_size=1
file_system=SequentialFileAllocation(block_size)
student_records=[
    StudentRecord("John Doe",101,10,"123 Main Street"),
    StudentRecord("Jane Smith",102,11,"456 Elm Street"),
    StudentRecord("Michael Brown",103,9,"789 Oak Street")
]
for record in student_records:
    file_system.add_record(record)
file_system.print_disk_status()
student_id=102
retrieved_record=file_system.get_record(student_id)
if retrieved_record:
    print(f"\n Retrieved Record for ID {student_id}:") 
    print(retrieved_record)
else:
    print(f"\n Record with ID {student_id} not found")