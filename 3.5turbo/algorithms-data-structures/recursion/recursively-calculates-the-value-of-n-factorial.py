def factorial_recursive(n):
    # Base case: if n is 0 or 1, return 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: calculate factorial of n-1 and multiply it with n
    else:
        return n * factorial_recursive(n - 1)

# Get user input for n
n = int(input("Enter a non-negative integer: "))

# Validate the input
if n < 0:
    print("Factorial is undefined for negative integers.")
else:
    result = factorial_recursive(n)
    print(f"The factorial of {n} is: {result}")
