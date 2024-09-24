class StudentRecord:
    def __init__(self, name, student_id, grade, address):
        self.name = name
        self.student_id = student_id
        self.grade = grade
        self.address = address

    def __str__(self):
        return f"Name: {self.name}, ID: {self.student_id}, Grade: {self.grade}, Address: {self.address}"

class SequentialFileAllocation:
    def __init__(self, block_size):
        self.block_size = block_size
        self.fat = {}
        self.next_free_block = 0

    def add_record(self, student_record):
        block_number = self.next_free_block
        self.fat[block_number] = student_record
        self.next_free_block += 1
        with open(f"student_record_{block_number}.txt", "w") as file:
            file.write(str(student_record))
        return True

    def get_record(self, student_id):
        for block_number in self.fat:
            with open(f"student_record_{block_number}.txt", "r") as file:
                record = file.read()
                fields = record.split(", ")
                student_id_field = fields[1].split(": ")[1]
                if student_id_field == str(student_id):
                    return record
        return None

    def print_disk_status(self):
        print(f"Next free block: {self.next_free_block}")
        print("File Allocation Table (FAT):")
        for block_number, record in self.fat.items():
            print(f"Block {block_number}: {record}")

# Driver Code
block_size = 1
file_system = SequentialFileAllocation(block_size)
student_records = [
    StudentRecord("John Doe", 101, 10, "123 Main Street"),
    StudentRecord("Jane Smith", 102, 11, "456 Elm Street"),
    StudentRecord("Michael Brown", 103, 9, "789 Oak Street")
]

for record in student_records:
    file_system.add_record(record)

file_system.print_disk_status()

student_id = 102
retrieved_record = file_system.get_record(student_id)
if retrieved_record:
    print(f"\nRetrieved Record for ID {student_id}:")
    print(retrieved_record)
else:
    print(f"\nRecord with ID {student_id} not found")