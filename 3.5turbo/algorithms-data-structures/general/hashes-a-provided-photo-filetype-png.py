import hashlib

def calculate_hash(file_path):
    # Read the file in binary mode
    with open(file_path, 'rb') as file:
        data = file.read()
    
    # Calculate the hash using sha256 algorithm
    hash_object = hashlib.sha256(data)
    hash_value = hash_object.hexdigest()
    return hash_value

def main():
    # Ask the user for the file path of the PNG photo
    file_path = input("Enter the file path of the PNG photo: ")
    
    try:
        # Calculate the hash of the photo
        hash_value = calculate_hash(file_path)
        
        # Print the hash value
        print("Hash of the photo:", hash_value)
    except FileNotFoundError:
        print("File not found!")

if __name__ == "__main__":
    main()
