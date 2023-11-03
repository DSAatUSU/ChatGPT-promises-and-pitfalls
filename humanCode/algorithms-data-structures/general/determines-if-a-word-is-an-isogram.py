# Determines if a word is an isogram


# Creating the function
def is_isogram(txt):
    to_lower = txt.lower()
  
    for letter in to_lower:
        if to_lower.count(letter) > 1:
            return False
        return True

# Assign user input
text = input("Enter any word. ")

#  Calculate result
result = is_isogram(text)

# Display result
print("Is the word", text, "an isogram:", result)
