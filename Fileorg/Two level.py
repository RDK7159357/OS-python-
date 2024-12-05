class TwoLevelDirectory:
    def __init__(self):
        self.users = {}

    def create_file(self, user, filename, content):
        if user not in self.users:
            self.users[user] = {}
        if filename in self.users[user]:
            print(f"Error: File '{filename}' already exists for user '{user}'.")
        else:
            self.users[user][filename] = content
            print(f"File '{filename}' created for user '{user}'.")

    def delete_file(self, user, filename):
        if user in self.users and filename in self.users[user]:
            del self.users[user][filename]
            print(f"File '{filename}' deleted for user '{user}'.")
        else:
            print(f"Error: File '{filename}' not found for user '{user}'.")

    def display_files(self, user):
        if user in self.users:
            print(f"User '{user}' Files:", self.users[user] or "None")
        else:
            print(f"Error: User '{user}' not found.")

# Example usage
two_level = TwoLevelDirectory()
two_level.create_file("user1", "file1", "Content of file1")
two_level.create_file("user1", "file2", "Content of file2")
two_level.create_file("user2", "file1", "Content of another file1")
two_level.display_files("user1")
two_level.delete_file("user1", "file2")
two_level.display_files("user1")
