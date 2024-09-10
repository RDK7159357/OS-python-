class PatientRecord: 
    def __init__(self, name, age,medical_id, address): 
        self.name = name         
        self.medical_id = medical_id 
        self.age = age 
        self.address = address 
 
    def __str__(self): 
        return f"Name: {self.name}, Age: {self.age}, Medical ID: {self.medical_id}, Address: {self.address}" 
 
class IndexedFileAllocation: 
    def __init__(self, block_size): 
        self.index_block_size = block_size 
        self.index_table = {}   
        self.next_free_block = 0 
        # self.disk_blocks = []   
 
    def add_record(self, patient_record): 
        self.index_table[self.next_free_block]=None
        block_number=self.next_free_block
        self.next_free_block+=1
        with open(f"patient_record_{block_number}.txt","w") as file:
            file.write(str(patient_record))
        # Write code here  
        return True 
 
    def get_record(self, medical_id): 
        for i in range(len(self.index_table)):
            with open(f"patient_record_{i}.txt","r") as file:
                record=file.read()
                fields=record.split(", ")
                medical_id_field=fields[2].split(": ")[1]
                if medical_id_field==str(medical_id):
                    return record
        return None
 
    def calculate_record_size(self, patient_record): 
        record_size=len(str(patient_record))
        return (record_size//self.index_block_size)+1 
 
    def print_disk_status(self): 
        print(f"Next free block: {self.next_free_block}")
 
# Driver Code     
index_block_size = 1 
file_system = IndexedFileAllocation(index_block_size)     
 
patient_records = [ 
        PatientRecord("John Smith", 45, 1001, "123 Hospital Road"), 
        PatientRecord("Jane Doe", 32, 1002, "456 Clinic Avenue"), 
        PatientRecord("Michael Johnson", 58, 1003, "789 Medical Plaza") 
    ]
for record in patient_records: 
  file_system.add_record(record) 
file_system.print_disk_status() 
medical_id = 1001
retrieved_record = file_system.get_record(medical_id) 
if retrieved_record: 
  print(f"\nRetrieved Record for Medical ID {medical_id}:") 
  print(retrieved_record) 
else: 
  print(f"\nRecord with Medical ID {medical_id} not found.") 