import hashlib

def string_hash(string):
    """
    Generates the hash of a given string using the SHA-256 algorithm.
    
    Args:
        string: Input string to be hashed.
        
    Returns:
        The string hash.
    """
    # Create a new SHA-256 hash object
    hash_object = hashlib.sha256()
    
    # Encode the input string to bytes
    encoded_string = string.encode('utf-8')
    
    # Update the hash object with the encoded string
    hash_object.update(encoded_string)
    
    # Get the resulting hash value
    hash_value = hash_object.hexdigest()
    
    return hash_value

# Main program
if __name__ == '__main__':
    # Get user input for the string
    input_string = input("Enter a string: ")
    
    # Calculate the hash of the input string
    hash_result = string_hash(input_string)
    
    # Print the hash result
    print("Hash result:", hash_result)
