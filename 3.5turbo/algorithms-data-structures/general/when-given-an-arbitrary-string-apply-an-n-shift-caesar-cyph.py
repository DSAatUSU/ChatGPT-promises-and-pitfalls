def caesar_cipher(text, shift):
    """
    Function to apply Caesar cipher to a given text with a given shift.
    :param text: The input text to encrypt.
    :param shift: The shift value for the cipher.
    :return: The encrypted string.
    """
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                encrypted_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                encrypted_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            encrypted_text += char
    return encrypted_text

# Get user input
text = input("Enter the text to encrypt: ")
shift = int(input("Enter the shift value: "))

# Apply Caesar cipher
encrypted_text = caesar_cipher(text, shift)

# Print the result
print("Encrypted text:", encrypted_text)

