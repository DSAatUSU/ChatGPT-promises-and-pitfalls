"""
This is a Python script that finds all numbers between 2000 and 3200 (both included)
which are divisible by 7 but not a multiple of 5. The numbers are printed in a comma-separated
sequence on a single line.
"""

# Initialize an empty list to store the numbers
numbers = []

# Iterate over the range from 2000 to 3201 (both included)
for num in range(2000, 3201):
    # Check if the number is divisible by 7 and not a multiple of 5
    if num % 7 == 0 and num % 5 != 0:
        # Append the number to the list
        numbers.append(str(num))

# Print the numbers as a comma-separated sequence on a single line
print(",".join(numbers))
