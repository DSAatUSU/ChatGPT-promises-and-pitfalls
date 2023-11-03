def is_isogram(word):
    # Convert the word to lowercase to eliminate case sensitivity
    word = word.lower()

    # Create an empty set to store the characters in the word
    characters = set()

    # Iterate through each character in the word
    for char in word:
        # If the character has already been encountered, it is not an isogram
        if char in characters:
            return False
        # Add the character to the set
        characters.add(char)

    # If we have iterated through all characters without returning False,
    # then the word is an isogram
    return True

# Ask the user for input
word = input("Enter a word: ")

# Check if the word is an isogram
if is_isogram(word):
    print(f"{word} is an isogram")
else:
    print(f"{word} is not an isogram")
