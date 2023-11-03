def sort_words_alphabetically(list_of_words):
    """
    Sorts a list of words alphabetically.
    """
    return sorted(list_of_words)


def print_words_separated_by_commas(list_of_words):
    """
    Prints a list of words separated by commas.
    """
    print("Sentence is: ", ", ".join(list_of_words))


if __name__ == "__main__":
    # Prompt the user to enter a comma-separated sequence of words
    words_input = input("Enter a comma-separated sequence of words: ")

    # Split the input into individual words
    words = words_input.split(",")

    # Sort the words alphabetically
    sorted_words = sort_words_alphabetically(words)

    # Print the sorted words
    print_words_separated_by_commas(sorted_words)
