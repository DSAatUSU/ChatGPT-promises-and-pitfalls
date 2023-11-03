# Ask the user for a sequence of comma-separated numbers
numbers = input("Enter a sequence of comma-separated numbers: ")

# Split the input into separate numbers
number_list = numbers.split(",")

# Use list comprehension to square each odd number
squared_odd_numbers = [int(number)**2 for number in number_list if int(number) % 2 != 0]

# Print the result
print(squared_odd_numbers)
