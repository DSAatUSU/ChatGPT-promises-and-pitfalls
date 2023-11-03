import numpy as np

def transpose_matrix():
    # Get the number of rows and columns in the matrix from the user
    num_rows = int(input("Enter the number of rows in the matrix: "))
    num_cols = int(input("Enter the number of columns in the matrix: "))
    
    # Initialize an empty matrix
    matrix = []
    
    # Get the matrix elements from the user
    print("Enter the matrix elements row by row:")
    for _ in range(num_rows):
        row = input().split()
        row = [float(element) for element in row]
        matrix.append(row)
    
    # Transpose the matrix using numpy
    transposed_matrix = np.transpose(matrix)
    
    # Print the transposed matrix
    print("Transposed matrix:")
    for row in transposed_matrix:
        print(row)

if __name__ == "__main__":
    transpose_matrix()
