import numpy as np

def multiply_vectors():
    # Get the user input for the first vector
    vector1 = input("Enter the first vector (separated by spaces): ")
    vector1 = list(map(int, vector1.split()))

    # Get the user input for the second vector
    vector2 = input("Enter the second vector (separated by spaces): ")
    vector2 = list(map(int, vector2.split()))

    try:
        # Multiply the vectors using numpy
        result = np.multiply(vector1, vector2)
        
        # Print the result
        print("Result: ", result)
    
    except ValueError:
        # Handle the exception if the vectors are not of the same length
        print("Error: Vectors must be of the same length")

if __name__ == "__main__":
    multiply_vectors()
