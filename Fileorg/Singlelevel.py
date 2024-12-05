class SingleLevelDirectory:
    def __init__(self):
        self.files = {}

    def create_file(self, name, content):
        if name in self.files:
            print(f"Error: File '{name}' already exists.")
        else:
            self.files[name] = content
            print(f"File '{name}' created.")

    def delete_file(self, name):
        if name in self.files:
            del self.files[name]
            print(f"File '{name}' deleted.")
        else:
            print(f"Error: File '{name}' not found.")

    def display_files(self):
        print("Files:", self.files or "None")

# Example usage
single_level = SingleLevelDirectory()
single_level.create_file("file1", "Content of file1")
single_level.create_file("file2", "Content of file2")
single_level.display_files()
single_level.delete_file("file1")
single_level.display_files()
