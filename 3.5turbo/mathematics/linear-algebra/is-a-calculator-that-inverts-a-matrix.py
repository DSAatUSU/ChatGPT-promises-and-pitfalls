import numpy as np

def invert_matrix():
    # Get user input for the matrix size
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))

    # Get user input for the matrix elements
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            elem = float(input(f"Enter the element for position ({i+1},{j+1}): "))
            row.append(elem)
        matrix.append(row)

    # Convert the matrix to a NumPy array
    np_matrix = np.array(matrix)

    try:
        # Invert the matrix
        inv_matrix = np.linalg.inv(np_matrix)
        print("The inverted matrix is:")
        print(inv_matrix)
    except np.linalg.LinAlgError:
        print("Cannot invert the matrix as it is singular.")

if __name__ == '__main__':
    invert_matrix()
