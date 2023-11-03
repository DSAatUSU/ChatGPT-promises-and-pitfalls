import numpy as np

def get_matrix():
    print("Input numbers separated by spaces representing each row in your matrix")
    print("E.g.: 1 2 3 4")
    print("Ensure that each row has the same number of arguments. Or there will be an error")
    print("Press enter on an empty line to finish adding rows to your matrix.")
    matrix = []
    inputString = 'none'
    while inputString != '':
        inputString = input("Enter your row (Empty for finished): ")
        if (inputString != ''):
            matrix.append([int(x) for x in inputString.split()])

    return np.array(matrix)


number = int(input("How many matrices would you like to multiply? "))

matrices = []
for i in range(number):
    matrices.append(get_matrix())

final = matrices[0]
i = 1
while i < len(matrices):
    final = np.matmul(final, matrices[i])
    i += 1

print(final)


