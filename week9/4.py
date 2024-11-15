import threading
import time
import random

class Document:
    def __init__(self):
        # Initialize a document with some lines of text
        self.lines = ["Line 1: Original text", "Line 2: Original text", "Line 3: Original text", "Line 4: Original text"]
        self.lock = threading.Lock()  # Lock to ensure thread-safe editing

    def edit_line(self, line_number, new_text):
        with self.lock:
            if 0 <= line_number < len(self.lines):
                print(f"Editing line {line_number + 1}: '{self.lines[line_number]}' -> '{new_text}'")
                self.lines[line_number] = new_text
            else:
                print(f"Line {line_number + 1} does not exist in the document.")

    def show_document(self):
        print("\nCurrent Document Content:")
        for line in self.lines:
            print(line)


def user_edit(document, user_id):
    # Simulate a user editing a random line in the document
    for _ in range(1):  # Each user makes 3 edits
        line_number = random.randint(0, len(document.lines) - 1)
        new_text = f"Edited by {user_id} at {time.time()}"
        document.edit_line(line_number, new_text)
        time.sleep(random.uniform(0.1, 0.3))  # Simulate time taken for each edit


# Driver Code
document = Document()
threads = []
user_ids = [f'User{i+1}' for i in range(2)]

for user_id in user_ids:
    t = threading.Thread(target=user_edit, args=(document, user_id))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

document.show_document()
print("\nAll user edits completed.")
