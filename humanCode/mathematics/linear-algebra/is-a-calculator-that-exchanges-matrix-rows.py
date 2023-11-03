print("Input numbers separated by spaces representing each row in your matrix")
print("E.g.: 1 2 3 4")
print("Ensure that each row has the same number of arguments.")
print("Press enter on an empty line to finish adding rows to your matrix.")
matrix = []
inputString = 'none'

while inputString != '':
    inputString = input("Enter your row (Empty for finished): ")
    if (inputString != ''):
        matrix.append([int(x) for x in inputString.split()])

first = int(input("Enter the first row to swap: [1-" + str(len(matrix)) + "]"))
other = int(input("Enter the second row to swap: [1-" + str(len(matrix)) + "]"))

matrix[first - 1], matrix[other - 1] = matrix[other - 1], matrix[first - 1]

print(matrix)

