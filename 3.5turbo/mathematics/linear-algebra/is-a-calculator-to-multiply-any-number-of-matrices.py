import numpy as np

def get_matrix_size(m):
    """
    Function to get the size (rows, columns) of a matrix.
    """
    return m.shape

def multiply_matrices(matrices):
    """
    Function to multiply the given matrices.
    """
    result = matrices[0]  # Start with the first matrix in the list
    
    for matrix in matrices[1:]:
        # Check if the dimensions of the matrices are compatible for multiplication
        if result.shape[1] != matrix.shape[0]:
            return None  # Matrices cannot be multiplied
        
        result = np.dot(result, matrix)
    
    return result

# Main program
if __name__ == "__main__":
    num_matrices = int(input("Enter the number of matrices: "))
    matrices = []
    
    for i in range(num_matrices):
        rows = int(input(f"Enter the number of rows for matrix {i+1}: "))
        columns = int(input(f"Enter the number of columns for matrix {i+1}: "))
        
        matrix = []
        print(f"Enter the elements for matrix {i+1}:")
        for j in range(rows):
            row = list(map(float, input().split()))
            matrix.append(row)
        
        matrices.append(np.array(matrix))
    
    result = multiply_matrices(matrices)
    
    if result is None:
        print("Matrices cannot be multiplied.")
    else:
        print("Result:")
        print(result)
