# 2. Managing Student Records in a Database using Sequential File Allocation
def manage_student_records(records):
    with open("students.txt", "w") as file:
        for record in records:
            file.write(f"{record['id']},{record['name']},{record['age']}\n")

    with open("students.txt", "r") as file:
        print("Student Records:")
        for line in file:
            print(line.strip())

students = [{'id': 1, 'name': 'Alice', 'age': 20}, {'id': 2, 'name': 'Bob', 'age': 22}]
manage_student_records(students)