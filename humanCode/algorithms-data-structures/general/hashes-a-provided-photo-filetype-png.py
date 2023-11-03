import hashlib

# General-purpose solution that can process large files
def file_hash(file_path):
    # https://stackoverflow.com/questions/22058048/hashing-a-file-in-python

    sha256 = hashlib.sha256()

    with open(file_path, "rb") as f:
        while True:
            data = f.read(65536)  # arbitrary number to reduce RAM usage
            if not data:
                break
            sha256.update(data)

    return sha256.hexdigest()


if __name__ == "__main__":
    # Ask the user for the file path of the PNG photo
    file_path = input("Enter the file path of the PNG photo: ")
    try:
        # Calculate the hash of the photo
        hash_value = file_hash(file_path)
        # Print the hash value
        print("Hash of the photo:", hash_value)
    except FileNotFoundError:
        print("File not found!")
