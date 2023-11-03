def print_even_length_words(string):
    # Split the string into words
    words = string.split()

    # Iterate over the words and print the even length words
    for word in words:
        if len(word) % 2 == 0:
            print(word)

# Ask the user to input a string
user_input = input("Enter a string: ")

# Call the function to print the even length words
print_even_length_words(user_input)
