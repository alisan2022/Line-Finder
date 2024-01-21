

def print_lines_with_requested_word(file_path,x):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                if x in line:
                    print(line.strip())
    except FileNotFoundError:
        print(f"The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


file_path = 'RomeoAndJuliet.txt'
word = 'Romeo'
print_lines_with_requested_word(file_path,word)