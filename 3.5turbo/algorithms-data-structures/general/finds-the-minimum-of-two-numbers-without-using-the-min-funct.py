def find_minimum(a, b):
    # Check if a is less than b
    if a < b:
        return a
    # Otherwise, b is the minimum
    else:
        return b


# Get user input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Call the function and print the result
minimum = find_minimum(num1, num2)
print("The minimum is:", minimum)
