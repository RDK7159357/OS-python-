class HierarchicalDirectory:
    def __init__(self):
        self.root = {}

    def create_file(self, path, filename, content):
        dirs = path.split("/")
        current = self.root
        for d in dirs:
            current = current.setdefault(d, {})
        if filename in current:
            print(f"Error: File '{filename}' already exists in '{path}'.")
        else:
            current[filename] = content
            print(f"File '{filename}' created in '{path}'.")

    def delete_file(self, path, filename):
        dirs = path.split("/")
        current = self.root
        for d in dirs:
            if d in current:
                current = current[d]
            else:
                print(f"Error: Path '{path}' not found.")
                return
        if filename in current:
            del current[filename]
            print(f"File '{filename}' deleted from '{path}'.")
        else:
            print(f"Error: File '{filename}' not found in '{path}'.")

    def display(self):
        print("Directory Structure:", self.root)

# Example usage
hierarchical = HierarchicalDirectory()
hierarchical.create_file("home/user1", "file1", "Content of file1")
hierarchical.create_file("home/user1", "file2", "Content of file2")
hierarchical.create_file("home/user2", "file1", "Content of another file1")
hierarchical.display()
hierarchical.delete_file("home/user1", "file1")
hierarchical.display()
