import os

def create_file(filename, content):
    """Creates a file with the given content."""
    with open(filename, 'w') as file:
        file.write(content)
    print(f"File '{filename}' created successfully.")

def read_file(filename):
    """Reads and prints the content of a file."""
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            content = file.read()
        print(f"Content of '{filename}':\n{content}")
    else:
        print(f"File '{filename}' does not exist.")

def delete_file(filename):
    """Deletes a file."""
    if os.path.exists(filename):
        os.remove(filename)
        print(f"File '{filename}' deleted successfully.")
    else:
        print(f"File '{filename}' does not exist.")

if __name__ == "__main__":
    while True:
        print("\nOptions:")
        print("1. Create a file")
        print("2. Read a file")
        print("3. Delete a file")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            filename = input("Enter filename: ")
            content = input("Enter file content: ")
            create_file(filename, content)
        elif choice == '2':
            filename = input("Enter filename: ")
            read_file(filename)
        elif choice == '3':
            filename = input("Enter filename: ")
            delete_file(filename)
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")
