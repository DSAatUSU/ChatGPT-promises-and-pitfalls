import numpy as np

def get_matrix_from_user():
    rows = int(input("Enter the number of rows: "))
    columns = int(input("Enter the number of columns: "))
    matrix = []

    for i in range(rows):
        row = []
        for j in range(columns):
            element = float(input(f"Enter the element at row {i+1}, column {j+1}: "))
            row.append(element)
        matrix.append(row)

    return np.array(matrix)

def rref(matrix):
    matrix_rref, _ = np.linalg.qr(matrix)

    for i in reversed(range(matrix_rref.shape[0])):
        nonzero_indices = np.nonzero(matrix_rref[i])[0]
        
        if len(nonzero_indices) == 0:
            continue
            
        leading_coefficient_index = nonzero_indices[0]
        leading_coefficient = matrix_rref[i, leading_coefficient_index]

        matrix_rref[i, :] /= leading_coefficient

        for j in reversed(range(i)):
            multiplier = matrix_rref[j, leading_coefficient_index]
            matrix_rref[j, :] -= multiplier * matrix_rref[i, :]
    
    return matrix_rref

if __name__ == '__main__':
    matrix = get_matrix_from_user()
    rref_matrix = rref(matrix)
    print("The row reduced echelon form (rref) of the matrix is:")
    print(rref_matrix)
