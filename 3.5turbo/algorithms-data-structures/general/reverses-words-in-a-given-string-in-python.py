def reverse_words(string):
    # Split the string into a list of words
    words = string.split()

    # Reverse the order of the words in the list
    reversed_words = words[::-1]

    # Join the reversed words back into a string
    reversed_string = ' '.join(reversed_words)

    return reversed_string

if __name__ == "__main__":
    # Ask the user to enter a string
    string = input("Enter a string: ")

    # Reverse the words in the string
    reversed_string = reverse_words(string)

    # Print the reversed string
    print("Reversed string:", reversed_string)
