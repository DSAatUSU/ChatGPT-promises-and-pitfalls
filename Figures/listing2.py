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

