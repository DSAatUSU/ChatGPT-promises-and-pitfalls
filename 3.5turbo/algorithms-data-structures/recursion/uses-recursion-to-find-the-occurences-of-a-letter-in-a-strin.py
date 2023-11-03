def count_occurrences(string, letter):
    # Base case: if the string is empty, return 0
    if len(string) == 0:
        return 0
    # Recursive case: check if the first character of the string is the letter
    # If it is, add 1 to the count and recursively call the function on the remaining string
    # If it isn't, simply recursively call the function on the remaining string
    return (1 if string[0] == letter else 0) + count_occurrences(string[1:], letter)


def main():
    # Get input from the user
    string = input("Enter a string: ")
    letter = input("Enter a letter: ")
    
    # Call the count_occurrences function and print the result
    count = count_occurrences(string, letter)
    print(f"The letter '{letter}' occurs {count} times in the string '{string}'.")


if __name__ == "__main__":
    main()
