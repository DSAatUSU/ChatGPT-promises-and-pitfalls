import numpy as np

def exchange_matrix_rows(matrix, row1, row2):
    # Copy the matrix
    new_matrix = np.copy(matrix)
    
    # Exchange the rows
    new_matrix[[row1, row2], :] = new_matrix[[row2, row1], :]
    
    return new_matrix

# Create a sample matrix
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

print("Original Matrix:")
print(matrix)

# Get input from the user
row1 = int(input("Enter the index of the first row to exchange: "))
row2 = int(input("Enter the index of the second row to exchange: "))

# Exchange the rows
new_matrix = exchange_matrix_rows(matrix, row1, row2)

print("\nMatrix after exchanging rows:")
print(new_matrix)
