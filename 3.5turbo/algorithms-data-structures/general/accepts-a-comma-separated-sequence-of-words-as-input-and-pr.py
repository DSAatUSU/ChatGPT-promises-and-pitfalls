# Prompt the user to enter a comma-separated sequence of words
words_input = input("Enter a comma-separated sequence of words: ")

# Split the input into individual words
words = words_input.split(",")

# Sort the words alphabetically
words.sort()

# Join the sorted words into a comma-separated sequence
sorted_words = ",".join(words)

# Print the sorted words
print(sorted_words)
