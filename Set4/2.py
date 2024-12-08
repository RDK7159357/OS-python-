# 11. Managing Medical Records in Hospital using Indexed File Allocation
def manage_medical_records(records):
    index_table = {record['id']: record for record in records}
    print("Medical Records (Indexed):")
    for key, value in index_table.items():
        print(f"Patient ID: {key}, Data: {value}")

medical_records = [
    {'id': 'P001', 'name': 'Alice', 'age': 30, 'ailment': 'Flu'},
    {'id': 'P002', 'name': 'Bob', 'age': 40, 'ailment': 'Diabetes'}
]
manage_medical_records(medical_records)