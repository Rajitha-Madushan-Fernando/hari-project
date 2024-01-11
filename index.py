file_path = 'c1.txt'
string_to_remove = "Messages with length"

try:
    with open(file_path, 'r') as file:
        for line in file:
            new_content = line.replace(string_to_remove, '')
            data = new_content.split(':')
            print(data[0])
except FileNotFoundError:
    print(f"file '{file_path}' not found.")
except Exception as e:
    print(f"An error occured: {e}")