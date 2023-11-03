import numpy as np

def get_matrix_size():
    """Asks the user for the matrix size and returns it as a tuple"""
    rows = int(input("Enter the number of rows in the matrix: "))
    cols = int(input("Enter the number of columns in the matrix: "))
    return (rows, cols)

def get_matrix_values(size):
    """Asks the user for the values of each element in the matrix,
    returns the matrix as a NumPy array"""
    matrix = np.zeros(size)
    rows, cols = size
    print("Enter the values of the matrix, row by row:")
    for i in range(rows):
        row_values = input(f"Enter the values for row {i+1} separated by spaces: ").split()
        for j in range(cols):
            matrix[i][j] = float(row_values[j])
    return matrix

def calculate_eigenvalues(matrix):
    """Calculates and returns the eigenvalues of a matrix"""
    eigenvalues = np.linalg.eigvals(matrix)
    return eigenvalues

if __name__ == '__main__':
    size = get_matrix_size()
    matrix = get_matrix_values(size)
    eigenvalues = calculate_eigenvalues(matrix)
    print("Eigenvalues:", eigenvalues)
