def count_characters(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print(f"Number of characters: {len(content)}")
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
        
def main():
    file_path = input("Enter the path to the file: ")
    count_characters(file_path)

if __name__ == "__main__":
    file_path = input("Enter the path to the file: ")
    count_characters(file_path)