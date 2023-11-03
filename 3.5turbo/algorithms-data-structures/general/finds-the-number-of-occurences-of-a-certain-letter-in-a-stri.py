def count_occurrences(string, letter):
    """
    Function to count the number of occurrences of a letter in a string.

    Args:
        string (str): The input string.
        letter (str): The letter to count the occurrences of.

    Returns:
        int: The number of occurrences of the letter in the string.
    """
    count = 0
    for char in string:
        if char == letter:
            count += 1
    return count

# Get user input for the string and the letter
string = input("Enter a string: ")
letter = input("Enter a letter: ")

# Call the function to count the occurrences
occurrences = count_occurrences(string, letter)

# Print the result
print("Number of occurrences of '{}' in '{}': {}".format(letter, string, occurrences))
