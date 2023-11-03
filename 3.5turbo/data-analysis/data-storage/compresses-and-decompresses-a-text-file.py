import zlib

def compress_file(file_path):
    """
    Compresses a text file using zlib compression algorithm.
    
    :param file_path: path to the text file
    """
    try:
        with open(file_path, 'rb') as file:
            input_data = file.read()
            compressed_data = zlib.compress(input_data, level=zlib.Z_BEST_COMPRESSION)
        
        with open(file_path + '.compressed', 'wb') as file:
            file.write(compressed_data)
        
        print('Compression successful. Compressed file saved as', file_path + '.compressed')
    except FileNotFoundError:
        print('File not found.')
    except Exception as e:
        print('An error occurred during compression:', str(e))

def decompress_file(file_path):
    """
    Decompresses a compressed text file using zlib decompression algorithm.
    
    :param file_path: path to the compressed file
    """
    try:
        with open(file_path, 'rb') as file:
            compressed_data = file.read()
            decompressed_data = zlib.decompress(compressed_data)
        
        with open(file_path[:-10], 'wb') as file:
            file.write(decompressed_data)
        
        print('Decompression successful. Decompressed file saved as', file_path[:-10])
    except FileNotFoundError:
        print('File not found.')
    except Exception as e:
        print('An error occurred during decompression:', str(e))

# Ask the user for input
file_path = input('Enter the path to the text file: ')

# Compress the file
compress_file(file_path)

# Decompress the file
decompress_file(file_path + '.compressed')
