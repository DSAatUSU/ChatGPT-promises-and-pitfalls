import json

def read_json_file(file_path):
    with open(file_path) as json_file:
        data = json.load(json_file)
    return data

def main():
    # Prompt the user for the JSON file path
    file_path = input("Enter the path to the JSON file: ")
    
    try:
        # Read the JSON file into a JSON object
        json_data = read_json_file(file_path)
        
        # Process the JSON data as needed
        # ...
        
        print("JSON file loaded successfully!")
    except FileNotFoundError:
        print("File not found!")
    except json.JSONDecodeError:
        print("Invalid JSON format!")

if __name__ == '__main__':
    main()
