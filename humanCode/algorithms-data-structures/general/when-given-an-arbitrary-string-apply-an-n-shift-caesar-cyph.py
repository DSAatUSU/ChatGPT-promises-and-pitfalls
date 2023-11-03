#A python program to illustrate Caesar Cipher Technique
def encrypt(text,s):
	result = ""

	# traverse text
	for i in range(len(text)):
		char = text[i]

		# Encrypt uppercase characters
		if (char.isupper()):
			result += chr((ord(char) + s-65) % 26 + 65)

		# Encrypt lowercase characters
		else:
			result += chr((ord(char) + s - 97) % 26 + 97)

	return result
if __name__ == "__main__":
    #check the above function
    text = str(input("Enter the text to encrypt: "))
    s = 4
    print ("Text : " + text)
    print ("Shift : " + str(s))
    print ("Cipher: " + encrypt(text,s))
