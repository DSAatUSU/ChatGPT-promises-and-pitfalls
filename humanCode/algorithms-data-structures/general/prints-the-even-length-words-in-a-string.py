def printWords(s):

    # split the string
    s = s.split(" ")

    # iterate in words of string
    for word in s:

        # if length is even
        if len(word) % 2 == 0:
            print(word)


# Driver Code
s = "ChatGPT is a large language model whcih can generate text based on the text given to it."
print("String: ", s)
print("Even length words:")
printWords(s)
