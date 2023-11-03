# Get the sequence of binary numbers from user
binary_numbers = input("Enter comma separated 4-digit binary numbers: ")

# Split the sequence by comma to get individual binary numbers
numbers = binary_numbers.split(",")

# Initialize an empty list to store the divisible numbers
divisible_numbers = []

# Iterate over each binary number
for number in numbers:
    # Convert binary number to decimal
    decimal = int(number, 2)
    
    # Check if the decimal number is divisible by 5
    if decimal % 5 == 0:
        # If divisible, add it to the divisible_numbers list
        divisible_numbers.append(number)

# Join the divisible_numbers list into a comma separated sequence
result = ",".join(divisible_numbers)

# Print the resulting sequence of divisible numbers
print("Divisible numbers: ", result)
