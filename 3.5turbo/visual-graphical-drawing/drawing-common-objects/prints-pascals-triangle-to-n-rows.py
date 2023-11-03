def print_pascals_triangle(n):
    triangle = [[1] * (i + 1) for i in range(n)]
    
    for i in range(n):
        for j in range(1, i):
            triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]
    
    for row in triangle:
        print(' '.join(str(num) for num in row))

# Get input from the user
n = int(input("Enter the number of rows for Pascal's triangle: "))

# Validate input
if n < 1:
    print("Number of rows should be greater than or equal to 1")
else:
    # Print Pascal's triangle
    print_pascals_triangle(n)
