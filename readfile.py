def read_file():
    filename = input("Enter the filename to read: ")
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("\nFile contents:")
            print(content)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except PermissionError:
        print(f"Error: Permission denied to read '{filename}'.")
    except Exception as e:
        print(f"Error: An unexpected error occurred: {e}")

def write_file():
    filename = input("Enter the filename to write: ")
    content = input("Enter the content to write: ")
    try:
        with open(filename, 'w') as file:
            file.write(content)
            print(f"\nSuccessfully wrote to '{filename}'")
    except PermissionError:
        print(f"Error: Permission denied to write to '{filename}'.")
    except Exception as e:
        print(f"Error: An unexpected error occurred: {e}")

def main():
    while True:
        print("\n=== File Management Program ===")
        print("1. Read a file")
        print("2. Write to a file")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ")
        
        if choice == '1':
            read_file()
        elif choice == '2':
            write_file()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()