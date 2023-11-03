def print_line(file_name, line_number):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            if line_number <= len(lines):
                line = lines[line_number - 1]
                print(line)
            else:
                print("Line number is out of range")
    except FileNotFoundError:
        print("File not found")

if __name__ == "__main__":
    file_name = input("Enter the file name: ")
    line_number = int(input("Enter the line number: "))
    print_line(file_name, line_number)
